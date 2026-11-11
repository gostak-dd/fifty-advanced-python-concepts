from multiprocessing import Process
import os

def worker(name):
    print(f"Process {name} is running in process ID: {os.getpid()}")

if __name__ == "__main__":
    process1 = Process(target=worker, args=("A",))
    process2 = Process(target=worker, args=("B",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both processes finished")

'''
Q: How does multiprocessing improve performance in CPU-bound tasks?
A: Multiprocessing improves performance in CPU-bound tasks by creating separate processes for each task.
Each process runs in its own memory space and can utilize multiple CPU cores, 
allowing for true parallel execution. This is especially beneficial for CPU-intensive operations,
as it can significantly reduce the overall execution time by distributing the workload across multiple cores.

Q: What is the difference between multithreading and multiprocessing in Python?
A: The main difference between multithreading and multiprocessing in Python lies in how they 
handle concurrency and parallelism:

- Multithreading: Involves multiple threads within a single process. Threads share the same memory space,
  which can lead to issues like race conditions. Due to Python's Global Interpreter Lock (GIL), 
  only one thread can execute Python bytecode at a time, making it less effective for 
  CPU-bound tasks but suitable for I/O-bound tasks.

- Multiprocessing: Involves multiple processes, each with its own memory space.
    This allows for true parallelism, as each process can run on a separate CPU core. 
    Multiprocessing is more effective for CPU-bound tasks, as it bypasses the GIL and can fully utilize 
    multiple cores for concurrent execution.
'''


