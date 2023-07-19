from work_place import WorkPlace, Consts
from math import *


class School(WorkPlace, Consts):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = floor(sqrt(self.level))

    def calc_costs(self):
        costs = Consts.BASE_PLACE_COST * floor(sqrt(self.level))
        return costs
