from microgrid.model.device import Device


class Load(Device):
    def __init__(self, name, capacity):
        super(Load, self).__init__(name)

        self.capacity = capacity
