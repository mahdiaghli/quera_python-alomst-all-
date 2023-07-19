from work_place import *
from math import *


class Mine(WorkPlace, Consts):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "mine"

    def calc_capacity(self):
        self.capacity = pow(self.level, 2)

    def calc_costs(self):
        costs = Consts.BASE_PLACE_COST + Consts.LEVEL_MUL * self.level
        return costs
