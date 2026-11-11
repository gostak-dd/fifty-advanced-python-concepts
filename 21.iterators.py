class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # An iterator must return itself.

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Signal the end of iteration.
        value = self.current
        self.current += 1
        return value

# Using the iterator
iterator = MyIterator(1, 5)
for num in iterator:
    print(num)  # Output: 1, 2, 3, 4

'''
Q: What is an iterator in Python, and how is it demonstrated in the provided code?
A: An iterator in Python is an object that implements the iterator protocol, which consists of the
methods `__iter__()` and `__next__()`. The `__iter__()` method returns the iterator object itself, and the
 `__next__()` method returns the next value from the sequence. In the provided code, 
 the `MyIterator` class is an example of a custom iterator that generates numbers from a 
 specified start to an end value. The `for` loop demonstrates how to use this iterator to iterate 
 through the generated numbers.
'''
