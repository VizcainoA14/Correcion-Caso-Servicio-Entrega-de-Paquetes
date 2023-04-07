class address:
    def __init__(self, Street: str = "", Neighborhood: str = "", Department: str = "") -> None:
        if type(Street) != str:
            print("Please enter a valid street.")
            return

        if type(Neighborhood) != str:
            print("Please enter a valid Neighborhood.")
            return

        if type(Department) != str:
            print("Please enter a valid Department.")

        self._street = Street
        self._neighborhood = Neighborhood
        self._department = Department

    @property
    def street(self) -> str:
        return self._street

    @street.setter
    def street(self, street_nuevo: int) -> None:
        if isinstance(street_nuevo, str):
            self._street = street_nuevo
        else:
            print("Please enter a valid street.")

    @property
    def neighborhood(self) -> str:
        return self._neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood_nuevo: int) -> None:
        if isinstance(neighborhood_nuevo, str):
            self._neighborhood = neighborhood_nuevo
        else:
            print("Please enter a valid Neighborhood.")

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, department_nuevo: int) -> None:
        if isinstance(department_nuevo, str):
            self._department = department_nuevo
        else:
            print("Please enter a valid Department.")

    def __str__(self) -> str:
        return f"""\nStreet: {self._street}, {self._neighborhood}, {self._department}"""

    def __eq__(self, other: 'address') -> bool:
        if not isinstance(other, address):
            return False

        return self._street == other._street and \
            self._neighborhood == other._neighborhood and \
            self._department == other._department


test_5 = address("72", "13 de junio")
print(test_5)
