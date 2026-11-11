class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance  # Controlled access

# Usage
account = BankAccount("Alice", 1000)
print(account.get_balance())  # Output: 1000

'''
Q: What is encapsulation in Python and how is it demonstrated in the BankAccount class?
A: Encapsulation is a fundamental concept in object-oriented programming that restricts direct access to an
    object's attributes and methods, promoting controlled access through public methods. 
    In the BankAccount class, encapsulation is demonstrated by making the balance attribute private 
    (using double underscores) and providing public methods (deposit, withdraw, and get_balance)
    to interact with it. This ensures that the balance can only be modified or accessed in a controlled
    manner, preventing unauthorized changes and maintaining data integrity.
'''