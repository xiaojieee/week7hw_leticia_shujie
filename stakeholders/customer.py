from stakeholders.person import Person


# Superclass (Person) is passed as a parameter in Customer class
# subclass inherits functionality and attributes from the superclass Person
class Customer(Person):

    # init is automatically used when class is called when it is being used to create a new object
    # constructor method - when it is classed the subclass no longer inherits from superclass
    # the subclass __init__ overrides the superclass
    # has to be in the exact same position or will pass parameters of baseclass and not consider order of subclass (show victoria)
    # this is only on the __init__ function
    # for example change gender and age to then run carlos code
    def __init__(self, firstname, lastname, gender, age, contact_details):
        # super function makes the subclass inherit all the methods and properties from superclass
        super().__init__(firstname, lastname, age, gender)
        # adding properties to customer profile
        self.products = []
        self.customer_id = self.generate_customer_id()
        self.contact_details = contact_details

    # use numCreated to give object unique number
    def generate_customer_id(self):
        customer_id = Person.numCreated + 1
        return f"0000{customer_id}"

    def purchase_product(self, product):
        # adds item to a list - I wonder if this will let
        self.products.append(product)
        return f"Purchased Products: '{product}'"

    # todo: REMOVE item from the event
    def return_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Item '{product}' returned.")
        else:  # try not to use else statement - what can i add
            print(f"Item '{product}' not found in customer's list.")

    # todo: properties for getters and setters
    #  properties are a way to encapsulate attributes of an object
    #  Properties allow you to define custom behavior when getting, setting, or deleting the value of an attribute.

    #  GETTERS: MAY CHANGE TO PROPERTIES
    # retrieve customer first and last name, age, contact details, customer id
    def get_customer_id(self):
        return self.customer_id

    def get_contact_details(self):
        return self.contact_details

    def get_product_list(self):
        return self.products

    # todo: SETTERS
    def set_contact_details(self, contact_details):
        self.contact_details = contact_details

    def isCustomer(self):
        return True

    def __str__(self):
        return (
            f"{'*' * 25}\nCUSTOMER ID: {self.customer_id}\nFirst Name: {self.get_firstname()}\nLast Name: {self.get_lastname()}"
            f"\nAge: {self.get_age()}\nContact Details: {self.get_contact_details()}\n"
            f"Purchases: {self.get_product_list()}\n{'*' * 25}")
