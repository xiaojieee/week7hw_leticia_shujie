from week7_let_homework.stakeholders.person import Person


class Employee(Person):

    # CONSTRUCTOR METHOD THAT CONTAINS THE ATTRIBUTES (DATA) OF SUBCLASS
    def __init__(self, firstname, lastname, age, gender, job_role, salary, department):
        # super function makes the subclass inherit all the methods and properties from superclass
        super().__init__(firstname, lastname, age, gender)
        self.job_role = job_role
        self.__salary = salary
        self.employee_id = self.generate_employee_id()
        self.department = department

    # use numCreated to give object unique number
    def generate_employee_id(self):
        employee_id = Person.numCreated + 1
        return f"0000{employee_id}"

    # GETTERS - used to retrieve information
    @property
    def job_role(self):
        return self.job_role

    @property
    def employee_id(self):
        return self.employee_id

    @property
    def department(self):
        return self.department

    @property
    def salary(self):
        return self.__salary

    # SETTERS
    @job_role.setter
    def job_role(self, new_job_role):
        self._job_role = new_job_role

    @employee_id.setter
    def employee_id(self, new_employee_id):
        self.employee_id = new_employee_id

    def set_department(self, new_department):
        self.department = new_department

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def isEmployee(self):
        return True

    def __str__(self):
        return (f"{'*' * 25}\nEMPLOYEE ID: {self.employee_id}\nFirst Name: {self.firstname}\n"
                f"Last Name: {self.lastname}\nJob Role: {self.get_job_role()}\n"
                f"Department: {self.get_department()}Salary: {self.get_salary()}\n{'*' * 25}")

    @job_role.setter
    def job_role(self, value):
        self._job_role = value

    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value

    @department.setter
    def department(self, value):
        self._department = value
