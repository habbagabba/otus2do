from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):

    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int | float = 0, max_cargo: int = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo: int = 0
        self.max_cargo: int = max_cargo

    def load_cargo(self, add_cargo: int):
        if self.cargo + add_cargo > self.max_cargo:
            raise exceptions.CargoOverload
        else:
            self.cargo += add_cargo

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
