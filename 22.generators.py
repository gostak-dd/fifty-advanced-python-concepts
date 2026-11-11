def my_generator():
    yield 1
    yield 2
    yield 3


# This defines a generator function but doesn't execute it
gen = my_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# print(next(gen))  # Raises StopIteration



def generator_with_send():
    value = yield "Start"
    yield f"Received: {value} again"

gen = generator_with_send()
print(next(gen))       # Output: Start
print(gen.send("Data"))  # Output: Received: Data
# print(gen.throw(ValueError))

'''
Q: What is a generator in Python, and how is it demonstrated in the provided code?
A: A generator in Python is a special type of iterator that allows you to iterate over a 
sequence of values lazily, meaning it generates values on the fly and does not store them in memory. 
Generators are defined using functions with the `yield` statement. In the provided code, 
`my_generator` is a simple generator function that yields three values (1, 2, and 3). 
The `generator_with_send` function demonstrates how to use the `send()` method to send a value back 
into the generator, allowing for two-way communication. The `throw()` method is also shown, which can be 
used to raise an exception inside the generator.
'''