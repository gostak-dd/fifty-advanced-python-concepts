# def call_counter(func):
#     def wrapper(*args, **kwargs):
#         wrapper.calls += 1
#         print(f"Call {wrapper.calls} to {func.__name__}")
#         return func(*args, **kwargs)
#     wrapper.calls = 0  # Add a counter attribute to the wrapper
#     return wrapper

# @call_counter
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")  # Call 1 to greet
# greet("Bob")    # Call 2 to greet

'''
Q: What is the purpose of the call_counter decorator?
A: The purpose of the call_counter decorator is to count the number of times a function is called. 
It adds a counter attribute to the wrapper function, which is incremented each time the function is called. 
This allows developers to track how many times a function is invoked, which can be useful for debugging 
or performance analysis.

Q: How does the call_counter decorator work?
A: The call_counter decorator works by defining a wrapper function that wraps around the original function. 
When the decorated function is called, the wrapper function is executed instead. Inside the wrapper,
the counter is incremented, and the original function is called with the provided arguments.

Q: Show the hierarchy of execution when the greet function is called.
A: When the greet function is called, the following hierarchy of execution occurs:
- The greet function is called with the argument "Alice".
- The call_counter decorator's wrapper function is executed.
- The counter is incremented.
- The original greet function is called with the argument "Alice".

'''


# So you can use decorators for caching
# def cache(func):
#     stored_results = {}
#     def wrapper(*args):
#         if args not in stored_results:
#             stored_results[args] = func(*args)
#         return stored_results[args]
#     return wrapper

# @cache
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)

# print(fib(10))  # Output: 55





# def authenticate(func):
#     def wrapper(*args, **kwargs):
#         print("Authenticating...")
#         return func(*args, **kwargs)
#     return wrapper

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Logging call to {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @authenticate
# @log
# def access_data():
#     print("Accessing sensitive data")

# access_data()
# Output:
# Authenticating...
# Logging call to access_data
# Accessing sensitive data

'''
Q: What is the purpose of the authenticate and log decorators?
A: The purpose of the authenticate decorator is to simulate an authentication process before 
executing the decorated function. It prints "Authenticating..." to indicate that authentication 
is taking place. The log decorator is used to log the call to the decorated function by printing a 
message that includes the function's name. Together, these decorators can be used to add authentication 
and logging functionality to a function without modifying its core logic.
'''



# def add_method(cls):
#     def new_method(self):
#         return "I am a new method!"
#     cls.new_method = new_method
#     return cls

# @add_method
# class MyClass:
#     pass

# obj = MyClass()
# print(obj.new_method())  # Output: I am a new method!

'''
Q: What is the purpose of the add_method decorator?
A: The purpose of the add_method decorator is to dynamically add a new method to a class. 
When applied to a class, it defines a new method (in this case, new_method) and attaches it to the class.
'''




import time

def timer(unit="seconds"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            if unit == "milliseconds":
                duration *= 1000
            print(f"{func.__name__} took {duration:.2f} {unit}")
            return result
        return wrapper
    return decorator

@timer(unit="milliseconds")
def slow_function():
    time.sleep(1)

slow_function()  # Output: slow_function took 1000.00 milliseconds

'''
Q: Explain the flow of execution when the slow_function is called.
A: When the slow_function is called, the following flow of execution occurs:
1. The slow_function is decorated with the timer decorator, which takes "milliseconds" as an argument.
2. The timer decorator returns the decorator function, which wraps the slow_function in the wrapper function.
3. The wrapper function is executed, which records the start time using time.time().
4. The original slow_function is called, which sleeps for 1 second.
5. After the slow_function completes, the end time is recorded.
6. The duration of the function execution is calculated by subtracting the start time from the end time.
7. If the unit is "milliseconds", the duration is converted to milliseconds.
8. The duration is printed to the console, showing how long the slow_function took to execute.
'''
