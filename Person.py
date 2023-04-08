class Person(object):  # Define the new class "Person"

    def __init__(self, dni: int = 0, name: str = "",
                 lastname: str = "") -> None:  # Creating the constructor of the class and initializing the variables

        # Validating the variables
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

    # Using property decorators
    @property
    def dni(self) -> int:  # Getter --> dni
        return self._dni

    @dni.setter  # Setter --> dni
    def dni(self, dni_new: int) -> None:
        if isinstance(dni_new, int):  # Validaitng the input variable for dni
            self._dni = dni_new
        else:
            print("Please enter a valid street.")

    @property
    def name(self) -> str:  # Getter --> name
        return self._firstName

    @name.setter  # Setter --> name
    def name(self, name_new: str) -> None:
        if isinstance(name_new, str):  # Validaitng the input variable for name
            self._firstName = name_new
        else:
            print("Please enter a valid first name.")

    @property
    def lastname(self) -> str:  # Getter --> lastname
        return self._lastname

    @lastname.setter  # Setter --> lastname
    def lastname(self, lastname_new: str) -> None:
        if isinstance(lastname_new, str):  # Validaitng the input variable for lastname
            self._firstName = lastname_new
        else:
            print("Please enter a valid last name.")

    def __str__(self) -> str:  # Defining "get info"
        return f"""\nDNI: {self._dni}\nName: {self._firstName} {self._lastname}"""

    def __eq__(self, other):  # Equal method, to compare that two objects are equal
        if isinstance(other, Person):
            return (self._dni == other._dni and
                    self._firstName == other._firstName and
                    self._lastname == other._lastname)
        return False


test_4 = Person(334, "Adrian", "Vizcaino")  # Prove variable
print(test_4)  # Print test
