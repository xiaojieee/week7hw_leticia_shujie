class Person:
    def __init__(self, firstname, lastname):
        self._first_name = firstname
        self._last_name = lastname


class Employee(Person):
    def __init__(self, firstname, lastname, employee_id, department):
        super().__init__(firstname, lastname)
        self._employee_id = employee_id
        self._department = department


class Customer(Person):
    def __init__(self, firstname, lastname, customer_id):
        super().__init__(firstname, lastname)
        self._balance = customer_id
