class BankAccount:
    """class representing a bank account
    """
    
    def __init__(self,account_balance = 0):
        
        self.account_balance = account_balance
        
    def deposit(self, amount):
        if amount <=0:
            return f"Amount must be positive"
        self.account_balance += amount 
        return self.account_balance

        
    def withdraw(self,amount):
        if self.account_balance -amount >= 0:
            return True
        

    def display_balance(self):
        return (f"Current Balance: ${self.account_balance}")
    
    
