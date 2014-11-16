
import os
import subprocess

from nose.tools import with_setup, raises

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

#TODO Test for route without semaphore
#TODO Test for semaphore without some colors

#########################
# Traffic Light Actions #
#########################

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

# Green state get/set duration

@with_setup(setup_sumo)
def test_get_green_light_duration():
    with Sumo() as sumo:
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        assert traffic_light.green_duration == 15000

@with_setup(setup_sumo)
def test_set_green_light_duration():
    with Sumo() as sumo:
        duration = 20000
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        traffic_light.green_duration = duration
        assert traffic_light.green_duration == duration

# Yellow state get/set duration

@with_setup(setup_sumo)
def test_get_yellow_light_duration():
    with Sumo() as sumo:
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        assert traffic_light.yellow_duration == 3000

@with_setup(setup_sumo)
def test_set_yellow_light_duration():
    with Sumo() as sumo:
        duration = 20000
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        traffic_light.yellow_duration = duration
        assert traffic_light.yellow_duration == duration

# Red state get/set duration

@with_setup(setup_sumo)
def test_get_red_light_duration():
    with Sumo() as sumo:
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        assert traffic_light.red_duration == 50000

@with_setup(setup_sumo)
def test_set_red_light_duration():
    with Sumo() as sumo:
        duration = 20000
        traffic_light = traffic_lights = sumo.get_all_traffic_lights()[0]
        traffic_light.red_duration = duration
        assert traffic_light.red_duration == duration

@raises(SystemExit)
def test_sumo_home_not_defined():
    """ Test Sumo instantiation without SUMO_HOME environment variable.
    This test must be run for last, otherwise other tests will fail.
    """
    del os.environ["SUMO_HOME"] #TODO find another way to test this without break other tests
    with Sumo() as sumo:
        pass
