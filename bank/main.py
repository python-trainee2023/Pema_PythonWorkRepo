from bank.account import SavingsAccount, CheckingAccount
from bank.transaction import deposit, withdraw, balance_enquiry

savings_account = SavingsAccount("9813850509", "Lana del rey", 10000.0)

deposit(savings_account, 100.0)

interest = savings_account.calculate_interest(2.5)
print(f"Savings Account Interest: ${interest:.2f}")

checking_account = CheckingAccount("111444", "abel", 500.0)

withdraw(checking_account, 150.0)

balance = balance_enquiry(checking_account)
print(f"Checking Account Balance: ${balance:.2f}")
