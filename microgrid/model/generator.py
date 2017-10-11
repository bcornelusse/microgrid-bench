from microgrid.model.device import Device


class Generator(Device):
    def __init__(self, name, params):

        super(Generator, self).__init__(name)

        self.capacity = None
        self.steerable = False
        self.min_stable_generation = 0.0

        for k in params.keys():
            if k in self.__dict__.keys():
                self.__setattr__(k, params[k])

        assert (self.capacity is not None)
