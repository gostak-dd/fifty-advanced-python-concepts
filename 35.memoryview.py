import sys
data = bytearray(b"A" * 10**6)
mv = memoryview(data)


# Slicing without copying
mv_slice = mv[100:100000]  # View of the data, no copy made

# Slicing with bytes
bytes_slice = data[100:100000]  # Creates a new copy

# Compare sizes
print(f"Size of memoryview slice: {sys.getsizeof(mv_slice):,} bytes")
print(f"Size of bytes slice: {sys.getsizeof(bytes_slice):,} bytes")

'''
Q: What is a memoryview in Python, and how does it differ from a regular bytes or bytearray object?
A: A memoryview in Python is an object that allows you to access the memory of another object 
(like bytes or bytearray) without copying the data. It provides a way to manipulate large data buffers 
efficiently, as it creates a view of the original data rather than duplicating it. This can 
lead to significant performance improvements when working with large datasets, as it avoids unnecessary 
memory allocation and copying. In contrast, slicing a bytes or bytearray object creates a new copy of 
the data, which can be less efficient in terms of both time and memory usage.

Q: When would you prefer bytes over memoryview, and vice versa, in Python programming?
A: You would prefer using bytes when you need an immutable sequence of bytes, such as when
working with fixed binary data that should not be modified. Bytes are suitable for scenarios where
the data is small or when you need to ensure that the data remains unchanged. 
On the other hand, you would prefer using memoryview when you need to work with large datasets or when 
you want to manipulate the data without creating copies. Memoryview is particularly useful for 
performance-critical applications, such as image processing, scientific computing, or any situation 
where you need to efficiently access and modify large buffers of binary data.

'''

