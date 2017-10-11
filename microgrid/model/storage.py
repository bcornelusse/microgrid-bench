from microgrid.model.device import Device


class Storage(Device):
    def __init__(self, name, params):

        super(Storage, self).__init__(name)

        self.capacity = None
        self.max_charge_rate = None
        self.max_discharge_rate = None
        self.charge_efficiency = 1.0
        self.discharge_efficiency = 1.0

        for k in params.keys():
            if k in self.__dict__.keys():
                self.__setattr__(k, params[k])

        assert (self.capacity is not None)
        assert (self.max_charge_rate is not None)
        assert (self.max_discharge_rate is not None)
