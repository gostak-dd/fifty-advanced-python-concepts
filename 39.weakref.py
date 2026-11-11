import weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

# Avoid circular references using weak references
a = Node("A")
b = Node("B")
a.next = weakref.ref(b)
b.next = weakref.ref(a) # type: ignore

# Access weak references
print(a.next().name)  # Output: "B"
print(b.next().name)  # Output: "A"

'''
Q: What is the purpose of using weak references in this code?
A: The purpose of using weak references in this code is to avoid circular references between the 
two Node instances (a and b). In a circular reference, each object holds a reference to the other, 
which can prevent them from being garbage collected, leading to memory leaks. By using weak references, 
the code allows the Node instances to be garbage collected when there are no strong references to them, 
thus preventing memory leaks and ensuring efficient memory management.
'''
