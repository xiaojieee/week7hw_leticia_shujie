from bond_account import BondAccount
from maximum_balance_breached_exception import MaximumBalanceBreachedException

# try block is what we want the code to do
try:
    lisa_bond_account = BondAccount("lisa", "Simpson", 500, 1000)
    print(lisa_bond_account)
    lisa_bond_account.deposit(200)
    print(lisa_bond_account)
    lisa_bond_account.deposit(900)
    print(lisa_bond_account)
    lisa_bond_account.deposit(200)
    print(lisa_bond_account)


# except is a catch block
except MaximumBalanceBreachedException as ex:
    print("@" * 25)
    print(f"An exception has occurred!")
    print(f"You are over the maximum amount allowed by ${ex.get_breach_amount()}")

else:
    print("no exception occurred")

# the final block will always print
finally:
    print("The FINALLY block always runs \n------------------------")
    print(lisa_bond_account)
