import os
import sys

sys.path.append(os.environ["SUMO_HOME"])

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

