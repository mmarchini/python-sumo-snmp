
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
