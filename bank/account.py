class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)

    def calculate_interest(self, interest_rate):
        return self.balance * (interest_rate / 100)


class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
