from Package import Package
from abc import abstractmethod


class Standar_Package(Package):
    @abstractmethod
    def __init__(self, id: int = 0, weight: float = 0,
                 description: str = "") -> None:
        self._fixedFee = 10000
        super().__init__(id, weight, description)
        self._cost = self.calculate()

    @abstractmethod
    def calculate(self) -> float:
        if self._weight <= 0.0 or self._weight > 50:
            print("\nPackage " + str(self._id) +
                  " is not a standard package")
            return 0
        calculation = (self._weight * self.W_GR_100 * 1000) + self._fixedFee
        return calculation

    def __str__(self) -> str:
        return super().__str__()

    def __eq__(self, other_Spackage: 'Standar_Package'):
        if isinstance(other_Spackage, Standar_Package):
            return super().__eq__(other_Spackage) and self._fixedFee == other_Spackage._fixedFee
        return False


test_3 = Standar_Package(37, 20, "descripcion paquete 37")

print(test_3)
