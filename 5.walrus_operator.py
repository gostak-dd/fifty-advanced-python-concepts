my_dict = {...}

def my_func(my_dict):
    my_var = my_dict.get("my_var", None)
    if my_var:
        return my_var

# With walrus operator
my_dict = {...}
def my_func(my_dict):
    if my_var := my_dict.get("my_var", None):
        return my_var

'''
Q: What is the walrus operator in Python?
A: The walrus operator (:=) is a new assignment operator introduced in Python 3.8.
    It allows you to assign a value to a variable as part of an expression,
    which can help to reduce code duplication and improve readability.
    Time Complexity: The time complexity of using the walrus operator is O(1) for
    simple assignments, as it performs a single assignment operation. However,
    the overall time complexity of the code block in which the walrus operator is used
    will depend on the specific operations being performed and the size of the data being processed.
'''