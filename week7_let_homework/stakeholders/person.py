# create a class with Person
# check and research about designing classes using OOP
# Consider appropriate constructors, properties, and methods for these classes
class Person:
    # read about numCreated which is an object to keep count pf objects created
    numCreated = 0

    # constructor function with attributes of the class
    # could I have date of birth ()
    # read more about the self so I can remember the importance of it. 
    def __init__(self, firstname, lastname, gender, age):
        self.first_name = firstname
        self.__last_name = lastname
        self._gender = gender
        self.__age = age
        self.full_name = firstname + " " + lastname

        Person.numCreated += 1

    # decorators allow you to define getter and setter for class attributes without explicitly calling them
    # @propert is used to define a method that acts as a "getter" for an attribute
    @property
    def first_name(self):
        return self.first_name.capitalize()

    @property
    def lastname(self):
        return self.__last_name.capitalize()

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self._gender

    # defines a setter for the attribute
    @first_name.setter
    def first_name(self, firstname):
        self.first_name = firstname

    @lastname.setter
    def lastname(self, lastname):
        self.__last_name = lastname

    # can you set what you can't get? Ask Victories if cannot find answer
    @gender.setter
    def gender(self, gender):
        self._gender = gender

        # properties allow you to create methods that behave like attributes
        # To check if this person is a customer

    # is instance method
    def isCustomer(self):
        return False

    # To check if this person is a customer
    def isEmployee(self):
        return False

    def __str__(self):
        return (f"First Name: {self.first_name}\nLast Name: {self.__last_name}"
                f"\nAge: {self.__age}\nGender: {self._gender}\n")
