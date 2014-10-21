import os, sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

import traci

def hello():
    PORT = 8813
    traci.init(PORT)
    traci.simulationStep()
    traci.simulationStep()
    vehicles = traci.vehicle.getIDList()
    print vehicles
    traci.close()

    return vehicles

