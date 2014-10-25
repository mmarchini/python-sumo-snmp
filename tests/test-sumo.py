
import subprocess

from nose.tools import with_setup

import sumoSNMP

def setup_sumo():
    subprocess.Popen(["sumo", "-c", "tests/fixtures/hello.sumo.cfg"])

@with_setup(setup_sumo)
def test_get_vehicles():
    with sumoSNMP.Sumo() as sumo:
        vehicles = sumo.get_all_vehicles()
        assert  vehicles == []
        sumo.step()
        vehicles = sumo.get_all_vehicles()
        assert  vehicles == ["veh0"]

@with_setup(setup_sumo)
def test_get_traffic_lights():
    with sumoSNMP.Sumo() as sumo:
        traffic_lights = sumo.get_all_traffic_lights()
        assert traffic_lights == ["-125"]

@with_setup(setup_sumo)
def test_get_traffic_light_state():
    with sumoSNMP.Sumo() as sumo:
        traffic_light = "-125"
        assert sumo.traffic_light_state(traffic_light) == "G"
        sumo.step(16)
        assert sumo.traffic_light_state(traffic_light) == "y"
        sumo.step(4)
        assert sumo.traffic_light_state(traffic_light) == "r"
        sumo.step(51)
        assert sumo.traffic_light_state(traffic_light) == "G"

