from person import Customer


class Account(Customer):
    """
    First name: customer's first name
    Last name: customer's last name
    Customer_id: customer's ID
    Initial_amount: customer's deposit amount
    @classmethod def set_bank_name: set name for the bank
    """
    numCreated = 0
    __bank_name = None

    def __init__(self, firstname, lastname, initial_amount):
        super().__init__(firstname, lastname, Account.numCreated)
        self._balance = initial_amount

        Account.numCreated += 1

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount >= 0:
            self._balance -= amount

    def __str__(self):
        return (f"Account\nFirst Name: {self.firstname}\nLast Name: {self.lastname}"
                f"\nCustomer ID: 0000{Account.numCreated}"
                f"\nBalance: ${self.balance}\n------------------------")

    # operator overloading

    def __add__(self, other):
        return self._balance + other.balance()
    # this will add the balance of the two instances

    def __gt__(self, other):
        return self._balance > other.balance()
    # if balance on left is greater, returns True, otherwise false

    def __lt__(self, other):
        return self._balance < other.balance()
    # if balance on right is greater, returns True, otherwise false

    def __eq__(self, other):
        return self.balance() == other.balance()
    # if both balance is equal, returns True

    # When using @property decorators, the "get" is not needed as it is treated as a property
    # note: properties are a way to encapsulate attributes of an object
    # note: Properties allow you to define custom behavior when getting, setting, or deleting the value of an attribute.

    @property
    def balance(self):
        return self._balance

    @property
    def firstname(self):
        return self._first_name

    @property
    def lastname(self):
        return self._last_name

    # When using @property.setter properties can now be set with the assignment operator

    @firstname.setter
    def firstname(self, new_firstname):
        self._first_name = new_firstname

    @lastname.setter
    def lastname(self, new_lastname):
        self._last_name = new_lastname

    @classmethod
    def get_bank_name(cls):
        return cls.__bank_name

    # When using @classmethod there would be no need to create an instance of the Account class

    @classmethod
    def set_bank_name(cls, name):
        cls.__bank_name = name

    @classmethod
    def get_customer_id(cls):
        return cls.numCreated


if __name__ == "__main__":
    lisa_account = Account('lisa', "s", 100)
    print(lisa_account)
    print(lisa_account.get_customer_id())
