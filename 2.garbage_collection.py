import gc
import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

# Create nodes
a = Node("A")
b = Node("B")
print(f"Initial ref count for a: {sys.getrefcount(a)}")  # One from 'a' variable
print(f"Initial ref count for b: {sys.getrefcount(b)}")  # One from 'b' variable

# Create circular reference
a.next = b
b.next = a
print("\nAfter creating circular reference:")
print(f"Ref count for a: {sys.getrefcount(a)}")  # Increased because b.next points to it
print(f"Ref count for b: {sys.getrefcount(b)}")  # Increased because a.next points to it

# Delete references
print("\nDeleting references...")
del a
del b
# Note: We can't print ref counts here because we can't access a or b anymore!

# Force garbage collection
collected = gc.collect()
print(f"\nGarbage collector collected {collected} objects")

'''
Interview Question: What is garbage collection in Python?
Answer: Garbage collection in Python is the process of automatically 
    identifying and freeing up memory that is no longer in use by the program. 
    Python uses reference counting and a cyclic garbage collector to manage memory. 
    When an object's reference count drops to zero, it is eligible for garbage collection. 
    The cyclic garbage collector can detect and clean up circular references that cannot be 
    freed by reference counting alone.
    Time Complexity: The time complexity of garbage collection can vary depending on the
    number of objects and the complexity of their relationships. In general,
    the time complexity of garbage collection is O(n), where n is the number of objects
    being tracked by the garbage collector. However, the actual time taken for garbage collection
    can be influenced by factors such as the frequency of garbage collection,
    the size of the heap, and the complexity of the object graph. In practice,
    garbage collection is usually efficient and does not significantly impact the performance
    of most Python programs.

Q: What is the difference between reference counting and cyclic garbage collection in Python?
A: Reference counting is a memory management technique where each object keeps track of 
the number of references pointing to it. 
When the reference count drops to zero, the object is immediately deallocated. 
However, reference counting cannot handle circular references, where two or more objects 
reference each other, preventing their reference counts from ever reaching zero.
Cyclic garbage collection, on the other hand, is a mechanism that can detect and clean up
circular references. It periodically scans the object graph to identify groups of objects
that form cycles and frees them.
'''