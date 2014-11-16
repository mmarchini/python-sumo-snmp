
class TrafficLightMib(object):
	"""Stores the data we want to serve.
	"""


	def __init__(self, traffic_light):
		self._traffic_light = traffic_light

	def getSysID(self):
		return self._traffic_light._id

	def setSysID(self, sysID):
		pass

	def getStatus(self):
		return self._traffic_light.state

	def getYellowDuration(self):
		return self._traffic_light.yellow_duration

	def getRedDuration(self):
		return self._traffic_light.red_duration
