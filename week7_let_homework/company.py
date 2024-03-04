from person import Employee


class Company(Employee):
    numCreated = 0
    __company_name = None

    def __init__(self, firstname, lastname, department):
        super().__init__(firstname, lastname, Company.numCreated, department)

        Company.numCreated += 1

    def __str__(self):
        return (f"Account\nFirst Name: {self.firstname}\nLast Name: {self.lastname}"
                f"\nEmployee ID: 0000{Company.numCreated}"
                f"\nDepartment: {self.department}\n------------------------")

    @property
    def firstname(self):
        return self._first_name.upper()

    @property
    def lastname(self):
        return self._last_name.upper()

    @property
    def department(self):
        return self._department

    @firstname.setter
    def firstname(self, new_firstname):
        self._first_name = new_firstname

    @lastname.setter
    def lastname(self, new_lastname):
        self._last_name = new_lastname

    @department.setter
    def department(self, new_department):
        self._department = new_department

    @classmethod
    def get_employee_id(cls):
        return cls.numCreated


if __name__ == "__main__":
    lisa_employee = Company("lisa", "simpson", "Accounting")
    print(lisa_employee)
    print(lisa_employee.get_employee_id())
