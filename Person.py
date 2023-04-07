class Person:

    def __init__(self, dni: int = 0, name: str = "",
                 lastname: str = "") -> None:

        if type(dni) != int:
            print("Please enter a valid DNI.")
            return

        if type(name) != str:
            print("Please enter a valid First Name.")
            return

        if type(lastname) != str:
            print("Please enter a valid last name.")

        self._dni = dni
        self._firstName = name
        self._lastname = lastname

    @property
    def dni(self) -> int:
        return self._dni

    @dni.setter
    def dni(self, dni_new: int) -> None:
        if isinstance(dni_new, int):
            self._dni = dni_new
        else:
            print("Please enter a valid street.")

    @property
    def name(self) -> str:
        return self._firstName

    @name.setter
    def name(self, name_new: str) -> None:
        if isinstance(name_new, str):
            self._firstName = name_new
        else:
            print("Please enter a valid first name.")

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, lastname_new: str) -> None:
        if isinstance(lastname_new, str):
            self._firstName = lastname_new
        else:
            print("Please enter a valid last name.")

    def __str__(self) -> str:
        return f"""\nDNI: {self._dni}\nName: {self._firstName} {self._lastname}"""

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self._dni == other._dni and
                    self._firstName == other._firstName and
                    self._lastname == other._lastname)
        return False


test_4 = Person(334, "Adrian", "Vizcaino")
print(test_4)
