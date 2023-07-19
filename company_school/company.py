from work_place import *


class Company(WorkPlace, Consts):
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "copmany"

    def calc_capacity(self):
        self.capacity = self.level

    def calc_costs(self):
        costs = Consts.BASE_PLACE_COST * self.level
        return costs

