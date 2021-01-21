#!/usr/bin/env python
import subprocess

import jitterentropy
import pytest


def test_version():
    ver = jitterentropy.version()
    assert ver == 3000100


def test_negative_bytes():
    with pytest.raises(jitterentropy.ReqError):
        jitterentropy.getrandbytes(-10)


def test_get_bytes():
    randbytes = jitterentropy.getrandbytes(16)
    bytestring = "".join("{:02x}".format(x) for x in randbytes)
    assert len(bytestring) == 32


def test_randomness(tmpdir):
    newFile = open(tmpdir / "bytes", "wb")
    # large values take a while
    newFileByteArray = bytearray(jitterentropy.getrandbytes(65536))
    newFile.write(newFileByteArray)
    newFile.close()

    result = subprocess.run(
        ["ent", "-b", tmpdir / "bytes"], stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    resulta = result.splitlines()
    line1 = resulta[0]
    tokens = line1.split()
    entropyval = float(tokens[2])
    assert entropyval >= 0.999
