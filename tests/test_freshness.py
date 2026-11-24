from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from threading import Barrier

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from syzygy_freshness import Cursor, Domain, Verifier, ZERO, fingerprint, reply

ROOT = Cursor(1, "root", "a"*64, 0, ZERO)
TIP = Cursor(2, "next", "b"*64, 1, "c"*64)
SUBJECT = fingerprint(["example","source"])
DOMAIN = Domain("authority","epoch","relationship","read-only")


@pytest.fixture
def env(tmp_path):
    key = Ed25519PrivateKey.generate()
    now = [10.]
    def open_db(enroll=False):
        return Verifier(tmp_path/"floor", DOMAIN, key.public_key(), ROOT,
                        enroll=enroll, clock=lambda: now[0])
    return open_db(True), key, now, open_db


def test_online_and_bounded_are_distinct(env):
    v,key,now,reopen = env
    assert v.observe(SUBJECT, lambda q: reply(key,q,TIP,"current")).status == "current_at_check"
    now[0] += .1
    assert v.bounded_preview(SUBJECT,max_age_ms=200).status == "bounded_as_of"
    assert reopen().bounded_preview(SUBJECT,max_age_ms=200).status == "unverified"
    now[0] += .2
    assert v.bounded_preview(SUBJECT,max_age_ms=200).status == "unverified"


@pytest.mark.parametrize("cursor", [ROOT,replace(TIP,head="e"*64),replace(TIP,publication_hash="d"*64)])
def test_rollback_or_equivocation_survives_restart(env,cursor):
    v,key,_,reopen=env
    v.observe(SUBJECT,lambda q:reply(key,q,TIP,"current"))
    assert v.observe(SUBJECT,lambda q:reply(key,q,cursor,"current")).reason == "history_conflict"
    assert reopen().observe(SUBJECT,None).reason == "quarantined"


def test_issuer_checks_extension_from_requested_floor(env):
    v,key,_,reopen=env
    assert v.observe(SUBJECT,lambda q:reply(key,q,TIP,"conflict")).reason == "history_conflict"
    assert reopen().observe(SUBJECT,None).reason == "quarantined"


def test_nonce_binding_unavailable_and_invalid_signer(env):
    v,key,_,_=env
    replay=[]
    def first(q):
        replay.append(reply(key,q,TIP,"current"))
        return replay[0]
    assert v.observe(SUBJECT,first).status == "current_at_check"
    assert v.observe(SUBJECT,lambda q:replay[0]).reason == "challenge_mismatch"
    other=Ed25519PrivateKey.generate()
    assert v.observe(SUBJECT,lambda q:reply(other,q,TIP,"current")).reason == "invalid_signature"
    def offline(q):
        raise ConnectionError
    assert v.observe(SUBJECT,offline).reason == "unavailable"


@pytest.mark.parametrize("delay",[2.0,-1.0])
def test_monotonic_time_interval(env,delay):
    v,key,now,_=env
    def late(q):
        now[0] += delay
        return reply(key,q,TIP,"current")
    assert v.observe(SUBJECT,late).reason == "timeout"


@pytest.mark.parametrize("packet", [None, [], [True], [{"bad":1},"00"*64]])
def test_malformed_reply(env,packet):
    v,_,_,_=env
    assert v.observe(SUBJECT,lambda q:packet).status == "unverified"


def test_concurrent_read_cannot_overwrite_advanced_floor(env):
    v,key,_,_=env
    barrier=Barrier(2)
    def exchange(q):
        barrier.wait(timeout=3)
        return reply(key,q,TIP,"current")
    with ThreadPoolExecutor(2) as pool:
        values=list(pool.map(lambda _:v.observe(SUBJECT,exchange).reason,range(2)))
    assert sorted(values)==["current","floor_changed"]


def test_trusted_root_change_requires_enrollment(tmp_path):
    key=Ed25519PrivateKey.generate()
    Verifier(tmp_path/"db",DOMAIN,key.public_key(),ROOT,enroll=True)
    with pytest.raises(ValueError,match="enrollment"):
        Verifier(tmp_path/"db",replace(DOMAIN,epoch="other"),key.public_key(),ROOT)


def test_wire_digest_golden():
    assert fingerprint(["example","source"]) == "15e54b37a39d7aa192ca06a3fec86b8c456118fc26157a06cada4cb01455742d"
