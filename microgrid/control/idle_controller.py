from microgrid.control.abstract_controller import AbstractController
from microgrid.simulate.gridaction import GridAction


class IdleController(AbstractController):
    def __init__(self, grid):
        super(IdleController, self).__init__(grid)

    def compute_actions(self, start_date, end_date, grid_state, horizon, debug=False):

        n_storages = len(self.grid.storages)

        zero_output = [0.0] * horizon

        grid_import = zero_output[:]
        grid_export = zero_output[:]
        production = zero_output[:]
        consumption = zero_output[:]
        state_of_charge = [zero_output[:] for b in range(n_storages)]
        charge = [zero_output[:] for b in range(n_storages)]
        discharge = [zero_output[:] for b in range(n_storages)]

        peak = 0.0
        peak_increase = 0.0

        return GridAction(grid_export=grid_export, grid_import=grid_import,
                          state_of_charge=state_of_charge,
                          charge=charge, discharge=discharge, production=production,
                          consumption=consumption,
                          peak=peak, peak_increase=peak_increase)
