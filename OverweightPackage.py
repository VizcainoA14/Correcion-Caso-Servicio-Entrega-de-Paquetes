from Package import Package
from abc import abstractmethod


class OverweightPackage(Package):
    @abstractmethod
    def __init__(self, id: int = 0, weight: float = 0,
                 description: str = "") -> None:
        self._Over_weight = 0
        self._cost_Ow = 3000
        super().__init__(id, weight, description)

        if self._weight < 50:
            print("\nPackage " + str(self._id) +
                  " is not a Over weight package")
            self._Over_weight = 0
            self._cost = 0
            return

        self._Over_weight = self._weight - 50
        self._cost = self.calculate()

    @abstractmethod
    def calculate(self) -> float:
        calculation = (self._weight * self.W_GR_100 * 1000) + \
            self._Over_weight * self._cost_Ow
        return calculation

    def __str__(self) -> str:
        return super().__str__()

    def __eq__(self, other_Spackage: 'OverweightPackage'):
        if isinstance(other_Spackage, OverweightPackage):
            return super().__eq__(other_Spackage) and self._Over_weight == other_Spackage._Over_weight and \
                self._cost == other_Spackage._cost
        return False


test_2 = OverweightPackage(36, 85, "descripcion paquete 36")

print(test_2)
