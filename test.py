
import subprocess

from nose.tools import with_setup

import hello


def setup_sumo():
    subprocess.Popen(["sumo", "-c", "hello.sumo.cfg"])

@with_setup(setup_sumo)
def test_hello():
    assert hello.hello() == ["veh0"]

