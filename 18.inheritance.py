class Animal:
    def __init__(self, name):
        print("Animal constructor called for ", name)
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"Dog(name={self.name}, age={self.age})"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        return f"{self.name} says Meow!"

    def __str__(self):
        return f"Cat(name={self.name}, age={self.age})"

# Usage
dog = Dog("Buddy", 3)
cat = Cat("Kitty", 2)
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Kitty says Meow!
print(dog)          # Output: Dog(name=Buddy, age=3)
print(cat)          # Output: Cat(name=Kitty, age=2)

'''
Q: What is inheritance in Python, and how is it demonstrated in the provided code?
A: Inheritance in Python is a mechanism that allows a class (called a subclass or derived
    class) to inherit attributes and methods from another class (called a superclass or base class).
    In the provided code, the `Dog` and `Cat` classes inherit from the `Animal` class. They override
    the `speak` method to provide their own implementation, demonstrating polymorphism. The `Animal`
    class serves as a base class, while `Dog` and `Cat` are subclasses that extend its functionality.

Q: what is super().__init__() in python?
A: In Python, `super().__init__()` is used to call the constructor of the parent class (superclass) 
from within a subclass. This allows the subclass to inherit and initialize attributes defined in the 
parent class. It is particularly useful when you want to extend or modify the behavior of the parent 
class while still retaining its initialization logic.
'''
