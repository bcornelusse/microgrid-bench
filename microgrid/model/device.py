from abc import ABCMeta
class Device(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.name = name