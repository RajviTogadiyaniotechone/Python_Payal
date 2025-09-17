# Create a class representing a simple Bank Account.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")


account1 = BankAccount("Payal", 1000)

# Checking the balance
account1.check_balance() 

# Withdrawing money
account1.withdraw(1500) 

# Depositing money
account1.deposit(2000)  

# Trying to withdraw more than the available balance
account1.withdraw(12000)  

# Checking balance again
account1.check_balance() 
