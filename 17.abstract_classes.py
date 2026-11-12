from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def concrete(self):
        return "Subscribe"

# Cannot instantiate an abstract class
# shape = Shape()  # Raises TypeError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Create an instance of the subclass
rect = Rectangle(4, 5)
print(rect.area())       # Output: 20
print(rect.perimeter())  # Output: 18
print(rect.concrete())

'''
Q: What is an abstract class in Python, and how is it used in the provided code?
A: An abstract class in Python is a class that cannot be instantiated on its own and is meant to be 
subclassed. It can contain abstract methods, which are methods that are declared but contain no 
implementation. Subclasses of an abstract class must implement all of its abstract methods in order to 
be instantiated.
'''
