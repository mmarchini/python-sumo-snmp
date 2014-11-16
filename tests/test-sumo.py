
import os
import subprocess

from nose.tools import with_setup

from sumoSNMP.sumo import Sumo

DEVNULL = open(os.devnull, 'wb')

def setup_sumo():
    subprocess.Popen(["sumo", "-c", "tests/fixtures/hello.sumo.cfg"],
        stderr=DEVNULL, stdout=DEVNULL)

@with_setup(setup_sumo)
def test_get_vehicles():
    with Sumo() as sumo:
        vehicles = sumo.get_all_vehicles()
        assert  vehicles == []
        sumo.step()
        vehicles = sumo.get_all_vehicles()
        assert  vehicles == ["veh0"]

@with_setup(setup_sumo)
def test_get_traffic_lights():
    with Sumo() as sumo:
        traffic_lights = sumo.get_all_traffic_lights()
        assert traffic_lights[0]._id == "-125"

@with_setup(setup_sumo)
def test_get_traffic_light_state():
    with Sumo() as sumo:
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        assert traffic_light.state == "G"
        sumo.step(16)
        assert traffic_light.state == "y"
        sumo.step(4)
        assert traffic_light.state == "r"
        sumo.step(51)
        assert traffic_light.state == "G"

#TODO Test for route without semaphore
#TODO Test for semaphore without some colors

@with_setup(setup_sumo)
def test_green_light_duration():
    with Sumo() as sumo:
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        assert traffic_light.green_duration == 15000

@with_setup(setup_sumo)
def test_yellow_light_duration():
    with Sumo() as sumo:
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        assert traffic_light.yellow_duration == 3000

@with_setup(setup_sumo)
def test_red_light_duration():
    with Sumo() as sumo:
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        assert traffic_light.red_duration == 50000
