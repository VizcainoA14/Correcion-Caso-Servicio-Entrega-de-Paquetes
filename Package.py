from abc import abstractmethod  # Importing the abstract method


class Package(object):  # Define principal class (Package)
    @abstractmethod  # Use abstract method
    def __init__(self, id: int = 0, weight: float = 0.0,
                 description: str = " "):  # Define constructor and initializing variables
        # Define conditionals for variables
        if type(id) != int:  # Validating that the incoming data is int
            print("Please enter a valid id.")
            return

        # Validating that the incoming data is float and greater than 0
        if weight < 0 and type(weight) != float:
            print("Please enter a valid weight.")
            return

        if type(description) != str:  # Validating that the incoming data is str
            print("Please enter a valid description.")
            return

        # Define variables
        self._id: int = id
        self._weight: float = weight
        self._description: str = description
        self.W_GR_100: float = 2
        self._cost: float = 0

    # Using decorators with property
    @property
    def id(self) -> int:  # Get id
        return self._id

    @id.setter  # Setter id
    def id(self, id_new: int) -> None:
        if id_new > 0 and isinstance(id_new, int):  # Validating
            self._id = id_new
        else:
            print("Please enter a valid id")

    @property
    def weight(self) -> float:  # Get weight
        return self._weight

    @weight.setter  # Setter weight
    def weight(self, weight_new: float) -> None:
        if weight_new > 0 and isinstance(weight_new, float):  # Validating
            self._weight = weight_new
        else:
            print("Please enter a valid weight.")

    @property
    def description(self) -> str:  # Get description
        return self._description

    @description.setter  # Setter description
    def description(self, description_new: str) -> None:  # Validating
        if isinstance(description_new, str):
            self._description = description_new
        else:
            print("Please enter a valid description.")

    @property
    def cost(self) -> float:  # Get cost
        return self._cost

    @abstractmethod  # Inheritable method
    def __str__(self) -> str:  # Method to print all the info
        return f"""\nId: {self._id}\nWeight: {self._weight}\ndescription: {self._description}\nShipping Cost: {self._cost}"""

    @abstractmethod  # Inheritable method
    def calculate(self) -> float:
        pass

    def __eq__(self, other_package: 'Package'):  # Equal method, to compare two objects
        if isinstance(other_package, Package):
            return self._id == other_package._id and self._weight == other_package._weight and \
                self._description == other_package._description
        return False


test_1 = Package(35, 10, "descripcion paquete 32")  # Prove test

print(test_1)  # Printing prove test
