from account import Account


# with @classmethod no instance of the Account class needs to be made before setting a bank name
Account.set_bank_name("Hello Bank!")
print(f"Welcome to {Account.get_bank_name()}")

lisa_account = Account("Lisa", "Simpson", 100)
print(lisa_account)
print(lisa_account.get_bank_name())
print(lisa_account.get_customer_id())

print(dir(Account))

marge_account = Account("Marge", "Simpson", 500)
print(marge_account)
print(marge_account.firstname)
print(marge_account.lastname)
# with property decorators, no need to use 'get'

# with the @property.setter in place, can now set names using assignment operator - equal sign
marge_account.lastname = "Bouvier"
print(marge_account)

marge_account.firstname = "Margorie"
print(marge_account)

bart_account = Account("Bart", "Simpson", 100)
print(bart_account)