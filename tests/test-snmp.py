
from sumoSNMP.snmp import SNMPAgent, MibObject
from sumoSNMP.snmp.proxies import traffic_light

def test_agent_creation():
	mib = traffic_light.TrafficLightMib(None)
	objects = [MibObject('TRAFFIC-MIB', 'sysID', mib.getSysID)]
	agent = SNMPAgent(objects)
	# try:
	# 	agent.serve_forever()
	# except KeyboardInterrupt:
	# 	print "Shutting down"
