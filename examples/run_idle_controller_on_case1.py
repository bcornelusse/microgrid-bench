import os
import json
from datetime import datetime

from microgrid.control import IdleController
from microgrid.forecast import Forecaster
from microgrid.history import Database
from microgrid.model import Grid
from microgrid.simulate import Simulator

# Simulation configuration
CASE = "case1"
SIMULATE_FROM_DATE = datetime(2015, 1, 1, 0, 0, 0)
SIMULATE_TO_DATE = datetime(2015, 6, 29, 0, 0, 0)
STORE_ACTIONS = True

# Definition of path to results and input
MICROGRID_CONFIG_FILE = "data/%s.json" % CASE
MICROGRID_DATA_FILE = 'data/%s_dataset.csv' % CASE
RESULTS_FOLDER = "results"
if not os.path.isdir(RESULTS_FOLDER):
    os.mkdir(RESULTS_FOLDER)
RESULTS_FILE = "%s/%s_out.json" % (RESULTS_FOLDER, CASE)

# Load the microgrid instance
with open(MICROGRID_CONFIG_FILE, 'rb') as jsonFile:
    data = json.load(jsonFile)
    microgrid = Grid(data)

# Build the forecaster
database = Database(MICROGRID_DATA_FILE, microgrid)
forecaster = Forecaster(database)

# Build the controller
controller = IdleController(microgrid)

# Build the simulator
simulator = Simulator(microgrid, controller, database)

# Run the simulation
grid_states = simulator.run(start_date=SIMULATE_FROM_DATE,
                            end_date=SIMULATE_TO_DATE)

# Export results
results = dict(dates=["%s" % d.date_time for d in grid_states],
               soc=[d.state_of_charge for d in grid_states],
               charge=[d.charge for d in grid_states],
               discharge=[d.discharge for d in grid_states],
               cum_total_cost=[d.cum_total_cost for d in grid_states],
               energy_cost=[d.energy_cost for d in grid_states],
               peak_cost=[d.peak_cost for d in grid_states],
               production=[d.production for d in grid_states],
               consumption=[d.consumption for d in grid_states],
               grid_import=[d.grid_import for d in grid_states],
               grid_export=[d.grid_export for d in grid_states])

if STORE_ACTIONS:
    results['actions'] = simulator.actions

with open(RESULTS_FILE, 'w') as jsonFile:
    json.dump(results, jsonFile)

from microgrid.plot import Plotter

plotter = Plotter(results, '%s/%s' % (RESULTS_FOLDER, CASE))
plotter.plot_results()
