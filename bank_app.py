import sys

from bond_account import BondAccount
from maximum_balance_breached_exception import MaximumBalanceBreachedException

# try block is what we want the code to do
try:
    lisa_bond_account = BondAccount("lisa", "Simpson", 500, 1000)
    print(lisa_bond_account)
    lisa_bond_account.deposit(900)
    print(lisa_bond_account)

    lisa_bond_account.withdraw(25)
    print(lisa_bond_account)

    lisa_bond_account.withdraw(10)
#     toggle between 10 and 100

# except is a catch block
except MaximumBalanceBreachedException as ex:
    print("@" * 10)
    print(f"An exception has occurred!")
    print(f"You would have breached your minimum balance by {ex.get_breach_amount()}")

else:
    print("no exception occurred")

# the final block will always print
finally:
    print("The FINALLY block always runs")
    print(lisa_bond_account)
