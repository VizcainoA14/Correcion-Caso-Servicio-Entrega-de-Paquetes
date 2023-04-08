class address(object): # Creating the new class address
    def __init__(self, Street: str = "", Neighborhood: str = "", Department: str = "") -> None: # Creating the cosntructor
        
        # Constraints
        if type(Street) != str:
            print("Please enter a valid street.")
            return

        if type(Neighborhood) != str:
            print("Please enter a valid Neighborhood.")
            return

        if type(Department) != str:
            print("Please enter a valid Department.")

        # Atributes 
        self._street = Street
        self._neighborhood = Neighborhood
        self._department = Department

    # Using properties
    @property
    def street(self) -> str: # Gettter --> street
        return self._street

    @street.setter # Setter --> street
    def street(self, street_nuevo: int) -> None:
        if isinstance(street_nuevo, str):
            self._street = street_nuevo
        else:
            print("Please enter a valid street.")

    @property
    def neighborhood(self) -> str:  # Gettter --> neighborhood
        return self._neighborhood

    @neighborhood.setter  # Settter --> street
    def neighborhood(self, neighborhood_nuevo: int) -> None:
        if isinstance(neighborhood_nuevo, str): 
            self._neighborhood = neighborhood_nuevo
        else:
            print("Please enter a valid Neighborhood.")

    @property
    def department(self) -> str:  # Gettter --> department
        return self._department

    @department.setter  # Settter --> street
    def department(self, department_nuevo: int) -> None:
        if isinstance(department_nuevo, str):
            self._department = department_nuevo
        else:
            print("Please enter a valid Department.")

    # Method for print __str__
    def __str__(self) -> str:
        return f"""\nStreet: {self._street}, {self._neighborhood}, {self._department}"""

    # Method equals
    def __eq__(self, other: 'address') -> bool:
        if not isinstance(other, address):
            return False

        return self._street == other._street and \
            self._neighborhood == other._neighborhood and \
            self._department == other._department


test_5 = address("72", "13 de junio") # Prove variable
print(test_5) # Print Test 
