from account import Account
from maximum_balance_breached_exception import MaximumBalanceBreachedException


class BondAccount(Account):

    def __init__(self, firstname, lastname, amount,  maximum_balance):
        super().__init__(firstname, lastname, amount)
        self._maximum_balance = maximum_balance

    def deposit(self, amount):
        if self._balance + amount > self._maximum_balance:
            raise MaximumBalanceBreachedException(self._balance + amount - self._maximum_balance)
        else:
            self._balance += amount
