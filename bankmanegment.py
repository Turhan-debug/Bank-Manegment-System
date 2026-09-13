import random

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number or random.randint(10000000, 99999999)
        self.account_holder = account_holder
        self.balance = balance
        
def check_balance(self):
        print(f"Current Balance: {self.balance}")
        
   


            
            
