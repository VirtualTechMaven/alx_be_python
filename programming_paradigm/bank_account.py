# bank_account.py

class BankAccount:
    """
    A simple Bank Account class demonstrating Object-Oriented Programming concepts.
    """

    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        Uses encapsulation to protect the account balance.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        Raises ValueError if the amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        """
        Return the account balance (for testing purposes).
        """
        return self.__account_balance
