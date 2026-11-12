from multiprocessing import Process, Value

def increment(shared_value):
    with shared_value.get_lock():  # Synchronize access
        shared_value.value += 1

if __name__ == "__main__":
    shared_value = Value('i', 0)  # Shared integer initialized to 0
    processes = [Process(target=increment, args=(shared_value,)) for _ in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(shared_value.value)  # Output: 5

'''
Q: What is the purpose of using `Value` in the above code snippet?
A: The purpose of using `Value` in the above code snippet is to create a shared
    memory object that can be safely accessed and modified by multiple processes. 
    `Value` allows us to store a single value (in this case, an integer) in shared memory, 
    enabling different processes to read and write to it without the need for complex inter-process 
    communication mechanisms. This is particularly useful for scenarios where we need to maintain
      a shared state across multiple processes.
'''
