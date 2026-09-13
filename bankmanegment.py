import random

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number or random.randint(10000000, 99999999)
        self.account_holder = account_holder
        self.balance = balance
        
def check_balance(self):
        print(f"Current Balance: {self.balance}")

def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
            print(f"New Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
            
def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"New Balance: {self.balance}")
            
name = input("Enter your name: ")

account = BankAccount(account_number=None, account_holder=name)

print("\nAccount created successfully!")
print(f"Name: {account.account_holder}")
print(f"Account Number: {account.account_number}")



        
   


            
            
