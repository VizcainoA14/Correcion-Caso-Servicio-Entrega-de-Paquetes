from Package import Package  # Importing class Package
from abc import abstractmethod  # Importing the abstract method


class OverweightPackage(Package):  # Creating the new class
    @abstractmethod  # Implementing abstract method
    def __init__(self, id: int = 0, weight: float = 0,
                 description: str = "") -> None:  # Definiting the constructor
        self._Over_weight = 0
        self._cost_Ow = 3000  # Definiting the value for the overweight
        super().__init__(id, weight, description)  # Inheritable variables

        if self._weight < 50:  # Validating that effectively is an Overweight Package
            print("\nPackage " + str(self._id) +
                  " is not a Over weight package")
            self._Over_weight = 0
            self._cost = 0
            return

        self._Over_weight = self._weight - 50
        self._cost = self.calculate()

    @abstractmethod  # Using the abstract method
    def calculate(self) -> float:  # Defining the method calculate
        calculation = (self._weight * self.W_GR_100 * 1000) + \
            self._Over_weight * self._cost_Ow
        return calculation  # Returning the operation "calculation"

    def __str__(self) -> str:  # Inheriting the principal print
        return super().__str__()

    # Method that verifies that an object is equal to another object.
    def __eq__(self, other_Spackage: 'OverweightPackage'):
        if isinstance(other_Spackage, OverweightPackage):
            return super().__eq__(other_Spackage) and self._Over_weight == other_Spackage._Over_weight and \
                self._cost == other_Spackage._cost
        return False


test_2 = OverweightPackage(36, 85, "descripcion paquete 36")  # Test variable

print(test_2)  # Print test
