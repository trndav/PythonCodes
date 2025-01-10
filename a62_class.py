# Class bank acc

class BankAccount:
    def __init__(self, balance):
        self.balance = balance 
    
    def balance_check(self):
        print(f"You have: {self.balance}")

    def deposit(self, amount):
        self.balance += amount 
        print(f"You have deposited: {amount}, and now you have: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount 
        print(f"You have withdraw: {amount}, and now you have: {self.balance}")

x = BankAccount(100)
x.balance_check()
x.deposit(50)
x.withdraw(30)