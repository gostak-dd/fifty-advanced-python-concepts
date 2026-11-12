# with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as file2:
#     data = file1.read()
#     file2.write(data)

























from contextlib import ExitStack

files = ['file1.txt', 'file2.txt']

with ExitStack() as stack:
    file_objects = [stack.enter_context(open(file, 'w')) for file in files]
    for file_obj in file_objects:
        file_obj.write("Hello, World!")

'''
Q: What is the purpose of using ExitStack in this code snippet, and how does it help manage multiple 
context managers?
A: The purpose of using ExitStack is to manage multiple context managers in a way that ensures 
they are properly exited, even if an exception occurs. It allows you to enter multiple context 
managers and exit them in the reverse order of their entry. This is particularly useful when you have a 
dynamic number of context managers to manage, as it provides a clean and efficient way to handle their 
lifecycle.
'''
