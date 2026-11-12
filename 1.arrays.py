from array import array

numbers = array('i', [1, 2, 3, 4, 5])
# i for integers

numbers.append(6)    # Add element to end
numbers.extend([7, 8])  # Add multiple elements
numbers.insert(0, 0)    # Insert at specific position

print(numbers)

## Explaination:
'''
Interview Question: What is an array in Python?
Answer: An array in Python is a data structure that can hold a fixed number of elements of
    the same data type. It is more efficient than a list for large amounts of data because 
    it uses less memory and provides faster access to elements. 
    The 'array' module in Python provides an array object that can be used 
    to create arrays of specific data types, such as integers or floats
    Time Complexity: The time complexity of accessing an element in an array is O(1),
    while the time complexity of inserting or deleting an element is O(n) in the worst case
'''