import random
from week7_let_homework.accounts.insufficient_funds_exception import InsufficientFundsException
# this is our capsule
# it's a collection of attributes and methods
# a class is an empty template that contains attributes and methods that can be used in objects
# ENCAPSULATION - class is an example as all data that is a member functions, varibles are encapsulated
class Account:
    # variables or objects we put in class level are shared across the objects of that class
    # both pieces of data are accessible through the class
    numCreated = 0
    # PRIVATE - bank name assigned to None
    __bank_name = None

    # this is a special method called the CONSTRUCTOR
    # a constructor method is used to get your object ready to be used
    # constructor define attributes and data so when instanciate to be used and fit for purpose
    def __init__(self, initial_amount, firstname, lastname):
        # _balance is an attribute, it's a piece of data
        # a single underscore means this field is semi-private
        self._balance = initial_amount
        self.first_name = firstname
        # dunder on a field means PRIVATE - KEEP OUT
        # double underscore means fully private
        self.__last_name = lastname
        self._account_holder_name = firstname + " " + lastname
        self._account_number = self.generate_account_number()  # Assigning unique account number

        # class field
        Account.numCreated += 1

    def generate_account_number(self):
        # Incrementing the total number of accounts created
        account_number = Account.numCreated + 1
        # Generating a random string of six digits
        # https://blog.finxter.com/python-how-to-generate-a-random-number-with-a-specific-amount-of-digits/
        # stringifies random integers from 0 - - to use string join function to get one string in 6 digits
        random_digits = ''.join(str(random.randint(0, 9)) for _ in range(7))
        # Combining the account number and random digits
        return f"{account_number}{random_digits}"

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        # validation
        if self._balance - amount < 0:
            raise InsufficientFundsException
        else:
            self._balance -= amount
    #   else situation we would raise an exception

    # this is what Java calls a getter
    # Java uses these to retrieve attribute values
    def get_balance(self):
        return self._balance

    #     create a getter method to retrieve the first_name attribute
    def get_firstname(self):
        return self.first_name

    def set_firstname(self, firstname):
        self.first_name = firstname

    #     create a getter method to retrieve the last_name attribute
    def get_lastname(self):
        return self.__last_name.upper()

    # getters READ and setters WRITE
    # getters RETURN something, setters do not
    # setters have parameters
    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname

    # getters can translate or modify the data before returning it
    # setters often validate the incoming data
    # setters often contain if statements

    # overriding a built-in method
    # override when inheriting from something and already exists, just changing the implementation of something
    def __str__(self):
        return (f"Account no: {self._account_number}\nFirstname: {self.get_firstname()}\n"
               f"Lastname: {self.get_lastname()}\nBalance: ${self.get_balance()}\n{'*' * 30}")

    # operator overloading
    def __add__(self, other):
        return self._balance + other.get_balance()

    def __gt__(self, other):
        return self._balance > other.get_balance()

    def __lt__(self, other):
        return self._balance < other.get_balance()

        #     PROPERTIES

        # @property
        # def mday(self):
        #     return self._day
        #
        # @mday.setter
        # def mday(self, day):
        #     self._day = day

    @property
    def account_holder_name(self):
        return self._account_holder_name

    @account_holder_name.setter
    def account_holder_name(self, name):
        self._account_holder_name = name
        name_parts = name.split()
        self.first_name = name_parts[0]
        self.__last_name = name_parts[1]

    #     CLASS Methods
    # retrieves the name of the bank is
    # decorator - extra functions (wrapping something around it)
    # this shared piece of code which can be accessed from the class
    # cls = class object parameter
    @classmethod  # these are decorators (annotations)
    def get_bank_name(cls):
        return cls.__bank_name

    # setter that sets the bank name
    @classmethod
    def set_bank_name(cls, name):
        cls.__bank_name = name

