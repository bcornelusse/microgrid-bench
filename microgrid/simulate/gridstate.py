class GridState:
    def __init__(self, grid, date_time):
        self.grid = grid
        n_storages = len(self.grid.storages)
        self.date_time = date_time

        # Arbitrarily set SOC at mid range at beginning of simulation
        self.state_of_charge = [s.capacity/2.0 for s in self.grid.storages]

        # Largest import over the last year to , per month
        self.past_peaks = [0.0] * 12

        self.cum_total_cost = 0.0 # EUR Cumulative total energy cost to date
        self.energy_cost = 0.0 # EUR
        self.peak_cost = 0.0 # EUR

        # Auxiliary info
        self.grid_import = 0.0
        self.grid_export = 0.0
        self.production = 0.0
        self.consumption = 0.0
        self.charge = [0.0] * n_storages
        self.discharge = [0.0] * n_storages
