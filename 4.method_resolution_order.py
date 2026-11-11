class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Output: Hello from A
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# The diamond problem

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    pass

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()  # Output: Hello from C
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

'''
Q: What is the method resolution order (MRO) in Python?
A: The method resolution order (MRO) in Python is the order in which base classes
are searched when looking for a method in a class hierarchy.

Q: How does Python determine the MRO for a class?
A: Python uses the C3 linearization algorithm to determine the MRO for a class.

Q: what is the diamond problem in Python?
A: The diamond problem in Python occurs when a class inherits from two classes
 that have a common base class. This can lead to ambiguity in method resolution, 
 as it may not be clear which method to call from the base class. 
 Python resolves this issue using the C3 linearization algorithm,
 which ensures a consistent and predictable method resolution order.

Q: what is c3 linearization algorithm in Python?
A: The C3 linearization algorithm is a method used in Python to determine the method 
resolution order (MRO) for classes in a multiple inheritance hierarchy. 
It ensures that the MRO is consistent and respects the order of base classes, 
while also handling the diamond problem. The algorithm works by merging the MROs of 
the base classes and ensuring that each class appears before its subclasses in the final MRO. 
This allows Python to resolve method calls in a predictable manner, even in complex inheritance scenarios.
'''