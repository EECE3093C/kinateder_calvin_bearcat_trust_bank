class Account:
    """A class representing a bank account."""

    # todo: Add the following methods:
    #       withdraw
    def __init__(self, account_number, account_holder_name, balance):
        """Initialize the account with the given account number, account holder name, and balance.

        Args:
            account_number (str): The account number.
            account_holder_name (str): The account holder name.
            balance (float): The account balance.
        """
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        """Deposit the given amount into the account."""
        self.balance += amount

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

    def display(self):
        """Display the account information."""
        print(
            f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: ${self.balance}"
        )


class SavingsAccount(Account):
    """A class representing a savings account."""

    # todo: Add the following method(s):
    #       __init__

    def calculate_interest(self):
        """Calculate and return the interest on the account balance."""
        return self.balance * (self.interest_rate / 100)

    def display(self):
        """Display the savings account information including the interest rate."""
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")


class CheckingAccount(Account):
    """A class representing a checking account."""

    # todo: Add the following methods:
    #       __init__

    def withdraw(self, amount):
        """Withdraw the given amount from the account if it doesn't exceed the overdraft limit."""
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Overdraft limit exceeded.")

    def display(self):
        """Display the checking account information including the overdraft limit."""
        super().display()
        print(f"Overdraft Limit: ${self.overdraft_limit}")
