"""Optional, observation-only freshness contract. SPDX-License-Identifier: MPL-2.0"""
from __future__ import annotations

from contextlib import closing
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
import secrets
import sqlite3
import time

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

PROFILE = "trivian.freshness.observation/1"
ZERO = "0" * 64
_HEX = re.compile("[0-9a-f]{64}")


def canonical(value):
    """The wire uses ordered lists of strings and unsigned interoperable integers."""
    return json.dumps(value, ensure_ascii=True, separators=(",", ":"), allow_nan=False).encode("ascii")


def fingerprint(value):
    return sha256(canonical(value)).hexdigest()


def _hex(value):
    return type(value) is str and _HEX.fullmatch(value) is not None


def _label(value):
    return type(value) is str and 0 < len(value) <= 256 and value.isascii() and value.isprintable()


@dataclass(frozen=True)
class Domain:
    issuer: str
    epoch: str
    relationship: str
    scope: str

    def __post_init__(self):
        if not all(_label(v) for v in self.wire()):
            raise ValueError("invalid enrolled domain")

    def wire(self):
        return [self.issuer, self.epoch, self.relationship, self.scope]


@dataclass(frozen=True)
class Cursor:
    revision: int
    event_id: str
    head: str
    publication: int
    publication_hash: str

    def __post_init__(self):
        for n in (self.revision, self.publication):
            if type(n) is not int or not 0 <= n < 2**53:
                raise ValueError("invalid revision")
        if (not self.revision or not _label(self.event_id) or not _hex(self.head)
                or not _hex(self.publication_hash) or (self.publication == 0) != (self.publication_hash == ZERO)):
            raise ValueError("incomplete source or publication anchor")

    def wire(self):
        return [self.revision, self.event_id, self.head, self.publication, self.publication_hash]


@dataclass(frozen=True)
class Query:
    domain: Domain
    subject: str
    nonce: str
    floor: Cursor

    def __post_init__(self):
        if not _hex(self.subject) or not _hex(self.nonce):
            raise ValueError("expected SHA-256 subject and 256-bit challenge")

    def wire(self):
        return [PROFILE, self.domain.wire(), self.subject, self.nonce, self.floor.wire()]


def reply(private_key, query, cursor, status):
    if status not in ("current", "stale", "unpublished", "conflict"):
        raise ValueError("invalid comparison")
    body = [query.wire(), cursor.wire(), status]
    return [body, private_key.sign(canonical(body)).hex()]


@dataclass(frozen=True)
class Observation:
    status: str
    reason: str
    subject: str
    domain: Domain
    cursor: Cursor | None


def _elapsed_time():
    if not hasattr(time, "CLOCK_BOOTTIME"):
        raise OSError("configure a trusted suspend-aware elapsed clock on this platform")
    return time.clock_gettime(time.CLOCK_BOOTTIME)


class Verifier:
    """One pinned authority/scope per private verifier DB. Reopen without enroll."""
    def __init__(self, path, domain, public_key, anchor, *, enroll=False, clock=_elapsed_time):
        self.domain, self.key, self.clock = domain, public_key, clock
        self.uri = Path(path).resolve().as_uri()
        self.cache = None
        self.identity = fingerprint([PROFILE, domain.wire(), anchor.wire(),
                                    public_key.public_bytes(Encoding.Raw, PublicFormat.Raw).hex()])
        with closing(sqlite3.connect(self.uri + ("?mode=rwc" if enroll else "?mode=rw"), uri=True)) as db, db:
            if enroll:
                db.execute("CREATE TABLE IF NOT EXISTS verifier(id INTEGER PRIMARY KEY, identity TEXT, floor TEXT, held INTEGER)")
                db.execute("INSERT OR IGNORE INTO verifier VALUES(1,?,?,0)", (self.identity, json.dumps(anchor.wire())))
            self._read(db)

    def _read(self, db):
        row = db.execute("SELECT identity,floor,held FROM verifier WHERE id=1").fetchone()
        if row is None or row[0] != self.identity:
            raise ValueError("authority enrollment mismatch")
        return Cursor(*json.loads(row[1])), bool(row[2])

    def _open(self):
        return sqlite3.connect(self.uri + "?mode=rw", uri=True, timeout=2)

    def _result(self, status, reason, subject, cursor=None):
        return Observation(status, reason, subject, self.domain, cursor)

    def observe(self, subject, exchange, *, timeout_ms=2000):
        """Exchange returns a decoded JSON reply. Transport must also enforce its own timeout."""
        if not _hex(subject) or type(timeout_ms) is not int or not 0 < timeout_ms <= 30000:
            raise ValueError("invalid subject or timeout")
        try:
            with closing(self._open()) as db:
                floor, held = self._read(db)
            if held:
                return self._result("unverified", "quarantined", subject)
            query = Query(self.domain, subject, secrets.token_hex(32), floor)
            start = self.clock()
            packet = exchange(query)
            if type(packet) is not list or len(packet) != 2:
                raise ValueError("invalid packet")
            body, signature = packet
            if type(body) is not list or len(body) != 3 or type(signature) is not str or len(signature) != 128:
                raise ValueError("invalid reply")
            echoed, point, status = body
            if type(point) is not list or len(point) != 5 or status not in ("current","stale","unpublished","conflict"):
                raise ValueError("invalid checkpoint")
            cursor = Cursor(*point)
            # Canonical comparison distinguishes booleans from integers.
            if canonical(echoed) != canonical(query.wire()):
                return self._result("unverified", "challenge_mismatch", subject)
            self.key.verify(bytes.fromhex(signature), canonical(body))
            with closing(self._open()) as db, db:
                db.execute("BEGIN IMMEDIATE")
                prior, held = self._read(db)
                elapsed = self.clock() - start
                if not 0 <= elapsed < timeout_ms / 1000:
                    return self._result("unverified", "timeout", subject)
                if prior != floor or held:
                    return self._result("unverified", "floor_changed", subject)
                if (status == "conflict" or cursor.revision < floor.revision
                        or cursor.publication < floor.publication
                        or (cursor.revision == floor.revision and
                            (cursor.head, cursor.event_id) != (floor.head, floor.event_id))
                        or (cursor.publication == floor.publication and cursor.publication_hash != floor.publication_hash)):
                    db.execute("UPDATE verifier SET held=1 WHERE id=1")
                    return self._result("unverified", "history_conflict", subject)
                if status in ("current", "stale") and cursor.publication == 0:
                    return self._result("unverified", "no_publication", subject)
                db.execute("UPDATE verifier SET floor=? WHERE id=1", (json.dumps(cursor.wire()),))
            outcome = self._result({"current":"current_at_check","stale":"stale",
                                    "unpublished":"unverified"}[status], status, subject, cursor)
            if status == "current":
                self.cache = (start, outcome)
            return outcome
        except InvalidSignature:
            return self._result("unverified", "invalid_signature", subject)
        except (OSError, sqlite3.Error):
            return self._result("unverified", "unavailable", subject)
        except (ValueError, TypeError, OverflowError, RecursionError):
            return self._result("unverified", "invalid_reply_or_state", subject)

    def bounded_preview(self, subject, *, max_age_ms):
        """One explicit content-free preview mode; local cache disappears on restart."""
        if not _hex(subject) or type(max_age_ms) is not int or not 0 < max_age_ms <= 1000:
            raise ValueError("preview bound must be between 1 and 1000 ms")
        item = self.cache
        if item and item[1].subject == subject:
            try:
                with closing(self._open()) as db:
                    current, held = self._read(db)
                if not held and current == item[1].cursor and 0 <= self.clock()-item[0] < max_age_ms/1000:
                    return self._result("bounded_as_of", "explicit_preview", subject, current)
            except (OSError, sqlite3.Error, ValueError):
                pass
        return self._result("unverified", "no_eligible_preview", subject)
