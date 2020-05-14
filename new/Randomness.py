from numpy import random

class Randomness:
    def __init__(self, _min, _max):
        self.min = _min
        self.max = _max
        self.value = 0

    def set_range(self, _min, _max):
        self.min = _min
        self.max = _max

    def get(self, _min=None, _max=None, range=False, values=None):
        if range and values:
            self.value = random.choice(values, replace=False)
        elif _min and _max:
            self.set_range(_min, _max)
            self.value = random.randint(self.min, self.max)
        return self.value

    def get_bool(self):
        self.value = random.choice([True, False])
        return self.value

