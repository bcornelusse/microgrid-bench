from .load import Load
from .storage import Storage
from .generator import Generator


class Grid:
    def __init__(self, data):
        self.loads = [Load(l["name"], l["capacity"]) for l in data["loads"]]
        self.generators = [Generator(g["name"], g) for g in data["generators"]]
        self.storages = [Storage(s["name"], s) for s in data["storages"]]

        self.base_purchase_price = data["base_purchase_price"]
        self.period_duration = data["period_duration"]
        self.peak_price = data["peak_price"]
        self.price_margin = data["price_margin"]

    @property
    def base_purchase_price(self):
        return self._base_purchase_price

    @base_purchase_price.setter
    def base_purchase_price(self, value):
        assert isinstance(value, int) or isinstance(value, float)
        self._base_purchase_price = float(value)

    @property
    def peak_price(self):
        return self._peak_price

    @peak_price.setter
    def peak_price(self, value):
        assert isinstance(value, int) or isinstance(value, float)
        self._peak_price = float(value)

    @property
    def period_duration(self):
        return self._period_duration

    @period_duration.setter
    def period_duration(self, value):
        assert isinstance(value, int) or isinstance(value, float)
        self._period_duration = float(value)

    @property
    def price_margin(self):
        return self._price_margin

    @price_margin.setter
    def price_margin(self, value):
        assert isinstance(value, int) or isinstance(value, float)
        self._price_margin = float(value)

    def purchase_price(self, energy_prices):
        return [self.base_purchase_price + p * (1 + self.price_margin) * 1e-3 for p in
                energy_prices]

    def sale_price(self, energy_prices):
        return [p * (1 - self.price_margin) * 1e-3 for p in energy_prices]
