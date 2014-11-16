import os, sys

from . import traffic_light

class Sumo(object):

    def __init__(self, port=8813):

        if 'SUMO_HOME' in os.environ:
            tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
            sys.path.append(tools)
        else:
            sys.exit("please declare environment variable 'SUMO_HOME'")

        self._traci = __import__("traci")

        self._traci.init(port)

    def __enter__(self,):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        self._traci.close()

    def step(self, steps=1):
        for i in range(steps):
            print "One more step!"
            self._traci.simulationStep()

    def get_all_vehicles(self):
        return self._traci.vehicle.getIDList()

    def get_all_traffic_lights(self):
        if not getattr(self, "_traffic_lights", None):
            traffic_lights = self._traci.trafficlights.getIDList()
            traffic_light_constructor = lambda id_: traffic_light.TrafficLight(self, id_)
            self._traffic_lights = map(traffic_light_constructor, traffic_lights)
        return self._traffic_lights
