class InsufficientFundsException(Exception):
    def __init__(self, overdrawn_account):
        self.overdrawn_account = overdrawn_account

    @property
    def overdrawn_amount(self):
        return self.overdrawn_account

    @overdrawn_amount.setter
    def overdrawn_amount(self, overdrawn_amount):
        self.overdrawn_account = overdrawn_amount
