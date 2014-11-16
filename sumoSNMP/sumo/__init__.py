import os, sys

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
            self._traci.simulationStep()

    def get_all_vehicles(self):
        return self._traci.vehicle.getIDList()

    def get_all_traffic_lights(self):
        if not getattr(self, "_traffic_lights", None):
            traffic_lights = self._traci.trafficlights.getIDList()
            traffic_light_constructor = lambda id_: TrafficLight(self, id_)
            self._traffic_lights = map(traffic_light_constructor, traffic_lights)
        return self._traffic_lights

def get_phase(phases, phase):
    return filter(lambda p: p._phaseDef.lower()==phase, phases).pop()

class TrafficLight(object):

    def __init__(self, sumo, _id):
        self._id = _id
        self._sumo = sumo

    @property
    def _complete_definition(self):
        return self._sumo._traci.trafficlights.getCompleteRedYellowGreenDefinition(self._id)[0]

    @_complete_definition.setter
    def _complete_definition(self, new_definition):
        self._sumo._traci.trafficlights.setCompleteRedYellowGreenDefinition(self._id, new_definition)

    @property
    def state(self):
        return self._sumo._traci.trafficlights.getRedYellowGreenState(self._id)

    @property
    def green_duration(self):
        phases = self._complete_definition._phases
        return get_phase(phases, "g")._duration

    @green_duration.setter
    def green_duration(self, duration):
        definition = self._complete_definition
        phase = get_phase(definition._phases, "g")
        phase_index = definition._phases.index(phase)
        phase._duration = duration
        phase._duration2 = duration
        phase._duration3 = duration
        self._complete_definition = definition

    @property
    def yellow_duration(self):
        phases = self._complete_definition._phases
        return get_phase(phases, "y")._duration

    @yellow_duration.setter
    def yellow_duration(self, duration):
        definition = self._complete_definition
        phase = get_phase(definition._phases, "y")
        phase_index = definition._phases.index(phase)
        phase._duration = duration
        phase._duration2 = duration
        phase._duration3 = duration
        self._complete_definition = definition

    @property
    def red_duration(self):
        phases = self._complete_definition._phases
        return get_phase(phases, "r")._duration

    @red_duration.setter
    def red_duration(self, duration):
        definition = self._complete_definition
        phase = get_phase(definition._phases, "r")
        phase_index = definition._phases.index(phase)
        phase._duration = duration
        phase._duration2 = duration
        phase._duration3 = duration
        self._complete_definition = definition
