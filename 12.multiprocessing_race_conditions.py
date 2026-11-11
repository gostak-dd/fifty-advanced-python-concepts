import multiprocessing

def increment(n):
    global counter
    for _ in range(100000):
        n.value += 1

if __name__ == '__main__':
    number = multiprocessing.Value('i', 0)
    p1 = multiprocessing.Process(target=increment, args=(number,))
    p2 = multiprocessing.Process(target=increment, args=(number,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(number.value)

'''
Q: What is a race condition in the context of multiprocessing?
A: A race condition in the context of multiprocessing occurs when multiple processes attempt to 
access and modify a shared resource (like a variable) concurrently, leading to 
unpredictable and incorrect results. In the provided code snippet, both processes are trying to 
increment the same `number` variable without any synchronization mechanism, which can result in 
lost updates and an incorrect final value.

Q: what happens if we use threads instead of processes in the above code snippet?
A: If we use threads instead of processes in the above code snippet, we would encounter issues 
related to Python's Global Interpreter Lock (GIL). The GIL allows only one thread to 
execute Python bytecode at a time, which means that even though we have multiple threads, 
they won't run in true parallelism for CPU-bound tasks. This can lead to performance bottlenecks 
and may not effectively utilize multiple CPU cores. Additionally, since threads share 
the same memory space, we would still face race conditions when accessing and modifying the
 shared `number` variable, leading to incorrect results unless proper synchronization mechanisms 
 (like locks) are used.

Q: Why would threading lead to race conditions in the above code snippet if we have GIL?
A: Even though Python's Global Interpreter Lock (GIL) allows only one thread to execute Python bytecode 
at a time, it does not prevent race conditions. Race conditions occur when multiple threads 
access and modify shared data concurrently without proper synchronization. In the provided code snippet, 
if we use threads instead of processes, both threads would still attempt to increment the shared 
`number` variable simultaneously. The GIL does not guarantee that the increments will be atomic, 
meaning that one thread could read the value of `number`, then another thread could read and 
modify it before the first thread writes back its incremented value. This can lead to lost 
updates and an incorrect final value of `number`, demonstrating that race conditions can still occur 
even with the GIL in place.
'''  