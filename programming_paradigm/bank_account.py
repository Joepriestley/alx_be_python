class BankAccount:
    """class representing a bank account
    """
    
    def __init__(self,account_balance = 0.0):
        
        self.account_balance = account_balance
        
    def deposit(self, amount):
        newAmount = self.account_balance =+ amount 
        return newAmount

        
    def withdraw(self,amount):
        if self.account_balance -amount >= 0:
            return True
        

    def display_balance(self):
        return (f"Current Balance: ${self.account_balance:.2f}")
    
    
