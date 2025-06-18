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
        if amount > self.account_balance:
            return f"Insufficient funds. Your account balance is: ${self.account_balance}"
        if amount <= self.account_balance:
            self.account_balance -=amount
            return f"${amount} withdrawn. Current Balance: ${self.account_balance} "
        

    def display_balance(self):
        return (f"Current Balance: ${self.account_balance}")

# joe_account =BankAccount()
# joe_account.deposit(70000)
# print(joe_account.withdraw(8000))
# print(joe_account.display_balance())
# account =BankAccount()
# account.deposit(3000)
# account.deposit(500)
# print(account.withdraw(300))
# print(account.display_balance())


