import os
import sys

from datetime import datetime

sys.path.insert(0, os.path.abspath('..'))

from microgrid.simulation import Simulation
from microgrid.control import IdleController

# Simulation configuration
CASE = "case1"
SIMULATE_FROM_DATE = datetime(2015, 1, 1, 0, 0, 0)
SIMULATE_TO_DATE = datetime(2015, 1, 2, 0, 0, 0)
simulation = Simulation(CASE, SIMULATE_FROM_DATE, SIMULATE_TO_DATE)

# Controller construction
controller = IdleController(simulation.microgrid)

# Simulation run
simulation.run(controller)
