class BankAccount:
    interest_rate = 0.03  # Default interest rate for all accounts

    def __init__(self, account_type, balance):
        self.account_type = account_type
        self.balance = balance

    @staticmethod
    def is_valid_transaction(amount):
        """Check if the transaction amount is valid."""
        return amount > 0

    @classmethod
    def create_savings_account(cls, initial_deposit):
        """Factory method to create a savings account."""
        if not cls.is_valid_transaction(initial_deposit):
            raise ValueError("Initial deposit must be positive.")
        return cls("Savings", initial_deposit)

    @classmethod
    def create_business_account(cls, initial_deposit):
        """Factory method to create a business account with a higher interest rate."""
        if not cls.is_valid_transaction(initial_deposit):
            raise ValueError("Initial deposit must be positive.")
        account = cls("Business", initial_deposit)
        account.interest_rate = 0.05  # Business accounts have a higher interest rate
        return account

# Example usage
try:
    # Utility function
    print(BankAccount.is_valid_transaction(-50))  # Output: False
    print(BankAccount.is_valid_transaction(100))  # Output: True
    b = BankAccount("commercial", 100)
    print(b.is_valid_transaction(100))

    # Creating accounts using class methods
    savings = BankAccount.create_savings_account(1000)
    business = BankAccount.create_business_account(5000)

    print(f"Savings Account - Balance: ${savings.balance}, Interest Rate: {savings.interest_rate}")
    # Output: Savings Account - Balance: $1000, Interest Rate: 0.03

    print(f"Business Account - Balance: ${business.balance}, Interest Rate: {business.interest_rate}")
    # Output: Business Account - Balance: $5000, Interest Rate: 0.05

except ValueError as e:
    print(e)

'''
Q: What is the difference between a static method and a class method in Python, 
and how are they used in the provided code?
A: 
In Python, a static method is a method that belongs to a class but does not have access to the 
instance (self) or class (cls) variables. It is defined using the @staticmethod decorator and is 
typically used for utility functions that do not require any information about the class or its instances. 
In the provided code, the `is_valid_transaction` method is a static method that checks if a transaction 
amount is valid.
Class methods, on the other hand, are methods that have access to the class itself and can modify class
-level attributes. They are defined using the @classmethod decorator and take `cls` as the first parameter.
In the provided code, the `create_savings_account` and `create_business_account` methods
are class methods that serve as factory methods to create instances of the `BankAccount` class.

'''
