class BankAccount:
    
    def __init__(self,account_balance = 0):
        
        self.account_balance = account_balance
        
    def deposit(self, amount):
    
        return self.account_balance += amount

    def withdraw(self,amount):
        if self.account_balance <= amount:
            return True
        else:
            False

    def display_balance(self):
        print(f"Current balance is ${self.account_balance}")
    
    
