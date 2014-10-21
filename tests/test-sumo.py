
import subprocess

from nose.tools import with_setup

import sumoSNMP


def setup_sumo():
    subprocess.Popen(["sumo", "-c", "tests/fixtures/hello.sumo.cfg"])

@with_setup(setup_sumo)
def test_get_vehicles():
    sumo = sumoSNMP.Sumo()
    vehicles = sumo.get_all_vehicles()
    assert  vehicles == []
    sumo.step()
    vehicles = sumo.get_all_vehicles()
    assert  vehicles == ["veh0"]
    sumo.close()

