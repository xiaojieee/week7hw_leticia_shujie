from week7_let_homework.accounts.account import Account
from week7_let_homework.accounts.account import InsufficientFundsException
from week7_let_homework.accounts.saving_account import SavingAccount

try:
    # code to be tested
    lisa_saving_account = SavingAccount(300, 'Lisa', 'Simpson', 250)
    lisa_account = Account(400, 'lisa', 'doyhle')
    print(lisa_account)
    print(lisa_saving_account)
    lisa_saving_account.deposit(50)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(25)
    print(lisa_saving_account)

    lisa_saving_account.withdraw(400)
#     toggle between 10 and 100

except InsufficientFundsException as ex:
    print("@" * 10)
    print(f"An exception has occurred!")
    print(f"You would have breached your minimum balance by {ex.get_breach_amount()}")

else:
    print("no exception occurred")

finally:
    print("The FINALLY block always runs")
    print(lisa_saving_account)


