class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Function demonstrating polymorphism
def print_area(shape):
    print(f"The area is {shape.area()}")

# Usage
rectangle = Rectangle(5, 10)
circle = Circle(7)

print_area(rectangle)  # Output: The area is 50
print_area(circle)     # Output: The area is 153.86

'''
Q: What is polymorphism in object-oriented programming, and how is it demonstrated in the provided code?
A: Polymorphism in object-oriented programming (OOP) refers to the ability of different classes to be 
treated as instances of the same class through a common interface. It allows methods to do different 
things based on the object that it is acting upon, even if they share the same method name.
'''