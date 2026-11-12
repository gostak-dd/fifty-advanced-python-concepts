from no_return_other import my_func

my_list = []

my_func(my_list, 5)
print(my_list)

'''
Q: why can you change the list in the function even though you don't return it?
A: In Python, when you pass a mutable object (like a list) to a function
, you are passing a reference to that object, not a copy of it. This means that 
any changes made to the object within the function will affect the original object
outside the function. In this case, when you pass `my_list` to `my_func`,
 the function appends elements to the same list object, so the changes are 
 reflected in `my_list` after the function call.
'''