from abc import abstractmethod


class Package(object):
    @abstractmethod
    def __init__(self, id: int = 0, weight: float = 0.0,
                 description: str = " "):
        if type(id) != int:
            print("Please enter a valid id.")
            return

        if weight < 0 and type(weight) != float:
            print("Please enter a valid weight.")
            return

        if type(description) != str:
            print("Please enter a valid description.")
            return

        self._id: int = id
        self._weight: float = weight
        self._description: str = description
        self.W_GR_100: float = 2
        self._cost: float = 0

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id_new: int) -> None:
        if id_new > 0 and isinstance(id_new, int):
            self._id = id_new
        else:
            print("Please enter a valid id")

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight_new: float) -> None:
        if weight_new > 0 and isinstance(weight_new, float):
            self._weight = weight_new
        else:
            print("Please enter a valid weight.")

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description_new: str) -> None:
        if isinstance(description_new, str):
            self._description = description_new
        else:
            print("Please enter a valid description.")

    @property
    def cost(self) -> float:
        return self._cost

    @abstractmethod
    def __str__(self) -> str:
        return f"""\nId: {self._id}\nWeight: {self._weight}\ndescription: {self._description}\nShipping Cost: {self._cost}"""

    @abstractmethod
    def calculate(self) -> float:
        pass

    def __eq__(self, other_package: 'Package'):
        if isinstance(other_package, Package):
            return self._id == other_package._id and self._weight == other_package._weight and \
                self._description == other_package._description
        return False


test_1 = Package(35, 10, "descripcion paquete 32")

print(test_1)
