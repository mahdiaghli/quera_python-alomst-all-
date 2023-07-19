from person import Person, Consts
from math import *


class Engineer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = "engineer"

    def get_price(self):
        price = floor(Consts.BASE_PRICE[self.job] * sqrt(Consts.MIN_AGE / self.age))
        return price

    def calc_life_cost(self):
        costs = floor(Consts.BASE_COST[self.job] * sqrt(self.age / Consts.MIN_AGE))
        return costs

    def calc_income(self):
        income = floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * sqrt(Consts.MIN_AGE / self.age))
        return income
