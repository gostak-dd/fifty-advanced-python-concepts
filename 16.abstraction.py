from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class.
    Defines a strict contract for all shapes.
    """

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass


class Rectangle(Shape):
    """
    Concrete implementation of Shape.
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


shape = Rectangle(5, 10)
print(shape.area())       
print(shape.perimeter())

'''
Q: What is abstract base class (ABC) in Python, and how is it used in the provided code?
A: An abstract base class (ABC) in Python is a class that cannot be instantiated on its own and is meant to 
serve as a blueprint for other classes. It defines a set of methods that must be implemented by any 
subclass that inherits from it. ABCs are defined using the `abc` module, which provides the `ABC` class 
and the `abstractmethod` decorator.
'''
