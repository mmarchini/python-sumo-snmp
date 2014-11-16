
import os
import time
import threading
import subprocess

import argparse
from ConfigParser import ConfigParser

from sumoSNMP.sumo import Sumo
from sumoSNMP.snmp import MibObject, SNMPAgent
from sumoSNMP.snmp.proxies import traffic_light

DEVNULL = open(os.devnull, 'wb')

def setup_sumo(sumo_config, sumo_gui=False):
	sumo_config = os.path.join(os.path.abspath("."), sumo_config)
	subprocess.Popen(["sumo%s"%(sumo_gui and "-gui" or ""), "-c", sumo_config],
		stderr=DEVNULL, stdout=DEVNULL)

def main():
	parser = argparse.ArgumentParser(description='Sumo SNMP server CLI tool.')

	parser.add_argument('--conf', '-c', dest='config_file', help='Configuration file.', required=True)

	args = parser.parse_args()

	config = ConfigParser()
	config.read(args.config_file)
	setup_sumo(config.get("global", "sumo.cfg"), config.getboolean("global", "sumo.gui"))
	with Sumo() as sumo:
		def _sumo_thread():
			while True:
				time.sleep(1)
				sumo.step()

		sumo_thread = threading.Thread(target=_sumo_thread)

		mib = traffic_light.TrafficLightMib(sumo.get_all_traffic_lights()[0])
		objects = [
			MibObject('TRAFFIC-MIB', 'sysID', mib.getSysID),
			MibObject('TRAFFIC-MIB', 'semStatus', mib.getStatus),
			MibObject('TRAFFIC-MIB', 'semTimeToRed', mib.getYellowDuration),
			MibObject('TRAFFIC-MIB', 'semTimeToGreen', mib.getRedDuration),
		]
		agent = SNMPAgent(objects)
		agent_thread = threading.Thread(target=lambda: agent.serve_forever())

		sumo_thread.start()
		agent_thread.start()

		sumo_thread.join()
		agent_thread.join()
