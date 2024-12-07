# Bank acc

class Bank:

    def __init__(self, balance):
        self.balance = balance 

    def check(self):
        return f"Balance: {self.balance}."
    
    def deposit(self):
        a = int(input("How much to deposit?\n"))
        self.balance += a 
        return f"Deposited: {a}. New balance is: {self.balance}."

    def withdraw(self):  
        b = int(input("How much to withdraw?\n"))
        if b <= self.balance:
            return f"You withdraw {b}. New balance is: {self.balance}."
        else:
            return f"You do not have that much."

x = Bank(0)
while True:
    usr = int(input("Choose one number:\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit\n"))

    if usr == 1:
        print(x.check())

    elif usr == 2:    
        print(x.deposit())

    elif usr == 3:
        print(x.withdraw())
    
    elif usr == 4:
        print(f"Exiting app.")
        break