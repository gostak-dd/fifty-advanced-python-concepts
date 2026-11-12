from collections import defaultdict

# Create a defaultdict with a default value of 0
default_dict = defaultdict(int)

default_dict['a'] += 1
default_dict['b'] += 5

print(default_dict)

'''
Q: What is a defaultdict in Python and how does it differ from a regular dictionary?
A: A defaultdict is a subclass of the built-in dict class in Python that provides a default
    value for a key that does not exist. When you try to access or modify a key that is not present 
    in the defaultdict, it automatically creates the key with the specified default value. 
    In contrast, a regular dictionary raises a KeyError if you try to access a key that does not exist. 
    This makes defaultdict particularly useful for counting or grouping items without having to check for 
    the existence of keys beforehand.
'''