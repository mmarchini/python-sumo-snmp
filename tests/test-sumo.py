
import subprocess

from nose.tools import with_setup

import sumoSNMP


def setup_sumo():
    subprocess.Popen(["sumo", "-c", "tests/fixtures/hello.sumo.cfg"])

@with_setup(setup_sumo)
def test_hello():
    assert sumoSNMP.hello() == ["veh0"]

