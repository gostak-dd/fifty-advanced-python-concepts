# from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper


# @my_decorator
# def greet(name):
#     """Greets a person by name."""
#     return f"Hello, {name}!"


# print(greet("Alice"))  # Output: Hello, Alice!
# print(greet.__name__)  # Output: greet
# print(greet.__doc__)   # Output: Greets a person by name.

'''
Q: What is the purpose of the @wraps decorator in the my_decorator function?
A: The purpose of the @wraps decorator in the my_decorator function is to preserve the metadata of 
the original function (func) when it is wrapped by the wrapper function. This includes attributes 
like __name__, __doc__, and others. Without @wraps, the wrapper function would replace these attributes, 
making it harder to introspect the original function. By using @wraps, we ensure that the decorated 
function retains its original identity and documentation, which is important for debugging and 
maintaining code.
'''


# from functools import lru_cache

# @lru_cache(maxsize=3)  # Cache up to 3 results
# def expensive_computation(x):
#     print(f"Computing {x}")
#     return x * x

# print(expensive_computation(2))  # Output: Computing 2, then 4
# print(expensive_computation(2))  # Output: 4 (from cache)

'''
Q: What is the purpose of the @lru_cache decorator in the expensive_computation function?
A: The purpose of the @lru_cache decorator in the expensive_computation function is to cache the 
results of the function calls, so that if the function is called again with the same arguments, 
it will return the cached result instead of recomputing it.
'''


from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)  # Multiplies all numbers
print(result)  # Output: 24

'''
Q: What is the purpose of the reduce function in the given code snippet?
A: The purpose of the reduce function in the given code snippet is to apply a binary function (in this case,
    a lambda function that multiplies two numbers) cumulatively to the items of the iterable 
    (the list of numbers), reducing the iterable to a single value. In this example, 
    it multiplies all the numbers in the list [1, 2, 3, 4] together, resulting in 24.
'''
