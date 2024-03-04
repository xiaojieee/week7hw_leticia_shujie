from stakeholders.person import Person
from stakeholders.customer import Customer
from stakeholders.employee import Employee

# creating objects for person
leticia = Person('leticia', 'santos', 'female', 28)
print(leticia)
print(f"{'*' * 40}")
print(leticia.firstname)
lastname = leticia.lastname
print(lastname)
print(leticia.full_name)
leticia.lastname = "Sequeira"
print(f"old last name: {lastname}\nnew last name: {leticia.lastname} ")
print(leticia.full_name)  # why does it not change to new last name

# todo: CUSTOMER MODULE (SUBCLASS METHODS)
# think about what type of customer or branch (shop)
# contact_details: cannot add 0 due to SyntaxError: leading zeros in decimal integer literals are not permitted
customer1 = Customer('carlos', 'salvador', '20', 'male', 7812345678)
print(customer1)
# issue - used append only adds one item, can't add anymore
# extends method iterates between each character - what can I use?
purchase = customer1.purchase_product('mobile phone')
# refund_item = carlos.return_product('mobile phone')
print(customer1)
first_name = customer1.firstname
print(f"{first_name}")
contact_details = customer1.get_contact_details()
customer1.set_contact_details('carlos@email.com')
print(f"Carlos old contact details: {contact_details} new contact details: {customer1.get_contact_details()}")
print(customer1.purchase_product('mobile phone'))
print(f"{'*' * 40}")
print(f"Total amount of Customers: {Customer.numCreated}")
print(customer1.isEmployee())
print(customer1.isCustomer())
print(f"{"*" * 40}")
# todo: EMPLOYEE MODULE (SUBCLASS METHOD)

# Creating instances of employees
employee1 = Employee('John', 'Doe', 30, 'Male', 'Software Engineer', 60000, 'Engineering')
print(employee1)
print(f"Employee ID: {employee1.get_employee_id()}")
print(f"Name: {employee1.firstname} {employee1.lastname}")
print(f"{"*" * 40}")

# updating employee details
salary = employee1.get_salary()
employee1.set_salary(65000)
print(f"Employee old salart {salary} and new salary {employee1.get_salary()}")
print(f"{"*" * 40}")
employee2 = Employee('Jane', 'Smith', 35, 'Female', 'Project Manager', 80000, 'Management')
print(employee2)
# retrieve data
print(f"Name: {employee2.firstname} {employee2.lastname}")
print(f"Salary: {employee2.get_salary()}")
# Updating employee details
department = employee2.get_department()
employee2.set_department('Human Resources')
print(f"old department {department} and new department {employee2.get_department()}")
print(f"{"*" * 40}")
# Checking if objects are instances of Employee class
print(f"Is employee1 an Employee? {employee1.isEmployee()}")
print(f"Is employee2 an Employee? {employee2.isEmployee()}")
print(f"{"*" * 40}")
# total amount of employees - THIS IS EMPLOYEES AND CUSTOMERS - OBJECT INSTANCES
print(Employee.numCreated)
