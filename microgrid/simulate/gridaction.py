import json

class GridAction():
    def __init__(self, grid_import, grid_export, production,
                 consumption, state_of_charge, charge,
                 discharge, peak, peak_increase):

        self.grid_import = grid_import
        self.grid_export = grid_export
        self.production = production
        self.consumption = consumption
        self.state_of_charge = state_of_charge
        self.charge = charge
        self.discharge = discharge
        self.peak = peak
        self.peak_increase = peak_increase

    def to_json(self):
        return self.__dict__
