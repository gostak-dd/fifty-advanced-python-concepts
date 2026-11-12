import threading
import time

def cpu_task():
    for _ in range(10**7):
        pass  # Simulates CPU work

threads = [threading.Thread(target=cpu_task) for _ in range(4)]

start = time.time()
thread = threading.Thread(target=cpu_task)
thread.start()
thread.join()
print(f"Time taken for single thread: {time.time() - start}")

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Time taken for multiple threads: {time.time() - start}")

'''
Q: What is the Global Interpreter Lock (GIL) in Python?
A: The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple 
native threads from executing Python bytecodes at once. This means that even in a multi-threaded Python program,
 only one thread can execute Python code at a time. 
 The GIL is necessary because CPython's memory management is not thread-safe.
'''
