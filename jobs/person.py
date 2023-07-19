import math


class Consts:
    # You can change these numbers to your custom prices
    BASE_PRICE = {'worker': 200, 'teacher': 150, 'engineer': 250}
    BASE_COST = {'worker': 200, 'teacher': 150, 'engineer': 300}
    BASE_INCOME = {'worker': {'mine': 800, 'school': 500, 'company': 600},
                   'teacher': {'mine': 400, 'school': 900, 'company': 700},
                   'engineer': {'mine': 1000, 'school': 800, 'company': 900}}
    MIN_AGE = 5
    AGE_MUL = 5


class Person:
    instances = []
    level = 1
    job = ""
    work_place = None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # level = 1
        # job = ""
        # work_place = None
        Person.instances.append(self)

    def do_level(self, income):
        return income * math.sqrt(self.level * self.work_place.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        return self.do_level(income) - cost

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1

    @staticmethod
    def calc_all():
        number = 0
        for i in Person.instances:
            number += Person.calc(i)
        return number
