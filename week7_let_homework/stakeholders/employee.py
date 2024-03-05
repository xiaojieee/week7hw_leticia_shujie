from week7_let_homework.stakeholders.person import Person


class Employee(Person):

    # CONSTRUCTOR METHOD THAT CONTAINS THE ATTRIBUTES (DATA) OF SUBCLASS
    @property
    def _department(self):
        return self.__department

    def __init__(self, firstname, lastname, age, gender, job_role, salary, department):
        # super function makes the subclass inherit all the methods and properties from superclass
        super().__init__(firstname, lastname, age, gender)
        self._job_role = job_role
        self.__salary = salary
        self._employee_id = self.generate_employee_id()
        self._department = department

    # use numCreated to give object unique number
    def generate_employee_id(self):
        employee_id = Person.numCreated + 1
        return f"0000{employee_id}"

    # GETTERS - used to retrieve information
    @property
    def job_role(self):
        return self._job_role

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def department(self):
        return self._department

    @property
    def salary(self):
        return self.__salary

    # SETTERS
    @job_role.setter
    def job_role(self, new_job_role):
        self._job_role = new_job_role

    @employee_id.setter
    def employee_id(self, new_employee_id):
        self._employee_id = new_employee_id

    @department.setter
    def department(self, new_department):
        self._department = new_department

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def isEmployee(self):
        return True

    def __str__(self):
        return (f"{'*' * 25}\nEMPLOYEE ID: {self._employee_id}\nFirst Name: {self.first_name}\n"
                f"Last Name: {self.lastname}\nJob Role: {self._job_role}\n"
                f"Department: {self._department}Salary: {self.salary}\n{'*' * 25}")

    @_department.setter
    def _department(self, value):
        self.__department = value
