class BankAccount:
    """Class representing a bank account."""

    def __init__(self, account_balance: float = 0.0):
        self.account_balance = account_balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount: float) -> bool:
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self) -> str:
        return f"Current Balance: ${self.account_balance:.2f}"
