from ground_vehicle import *
from flying_vehicle import *


class Airplane(FlyingVehicle, GroundVehicle):
    def __init__(self, airline, number_of_crew, captain, **kwargs):
        super().__init__(**kwargs)
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain


class B707(Airplane):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
