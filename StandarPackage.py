from Package import Package  # Import the parent class Package
from abc import abstractmethod  # Import the abstract method


class Standar_Package(Package):  # Defining the new class from the parent class Package
    @abstractmethod  # Implementing the abstract method
    def __init__(self, id: int = 0, weight: float = 0,
                 description: str = "") -> None:  # Creating the constructor
        self._fixedFee = 10000
        super().__init__(id, weight, description)  # Inherited variables
        # New variable that gets its value from the method calculate
        self._cost = self.calculate()

    @abstractmethod  # Using the abstract method
    def calculate(self) -> float:  # Implementing the new method
        if self._weight <= 0.0 or self._weight > 50:
            print("\nPackage " + str(self._id) +
                  " is not a standard package")
            return 0  # Exit in case the method is fulfilled
        calculation = (self._weight * self.W_GR_100 * 1000) + self._fixedFee
        return calculation  # Return of the method

    def __str__(self) -> str:  # Principal print or "get info"
        return super().__str__()

    # Comparing two objects and verifying that they are the same
    def __eq__(self, other_Spackage: 'Standar_Package'):
        if isinstance(other_Spackage, Standar_Package):
            return super().__eq__(other_Spackage) and self._fixedFee == other_Spackage._fixedFee
        return False


# Creating a prove or test variable
test_3 = Standar_Package(37, 20, "descripcion paquete 37")

print(test_3)  # Printing the test
