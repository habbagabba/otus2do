from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int | float = 0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        fuel_needs = distance * self.fuel_consumption
        if fuel_needs <= self.fuel:
            self.fuel -= fuel_needs
        else:
            raise NotEnoughFuel
