import dis 

def count_to_ten():
    for i in range(10):
        print(i)

dis.dis(count_to_ten)

'''
Q: What is Python bytecode, and how does the `dis` module help in understanding it?
A: Python bytecode is an intermediate representation of Python code that is executed by the Python interpreter.
The `dis` module in Python allows developers to disassemble Python functions and view their bytecode instructions.
By using `dis.dis()`, you can see the low-level operations that the Python interpreter performs
when executing a function, which can help in understanding performance characteristics and debugging.
'''
