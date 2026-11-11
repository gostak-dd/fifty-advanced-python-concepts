def validate(data, *validators):
    for validator in validators:
        if not validator(data):
            return False
    return True

# Validators
is_non_empty = lambda x: bool(x)
is_alpha = lambda x: x.isalpha()

# Validate input
input_data = "Python"
is_valid = validate(input_data, is_non_empty, is_alpha)
print(is_valid)  # Output: True

'''
Q: What are higher-order functions in Python, and how is the `validate` function an example of this concept?
A: Higher-order functions in Python are functions that can take other functions as arguments, 
return functions as their result, or both. They allow for more abstract and flexible programming 
by enabling the use of functions as first-class citizens.
The `validate` function is an example of a higher-order function because it takes a variable 
number of validator functions as arguments (using *validators) and applies them to the input data. 
It checks if the input data passes all the provided validation functions, demonstrating how functions 
can be passed and used within another function.
'''