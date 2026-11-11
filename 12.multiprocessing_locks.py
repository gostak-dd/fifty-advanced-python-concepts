
import multiprocessing

def increment(n, lock):
    for _ in range(100000):
        with lock:
            n.value += 1

if __name__ == '__main__':
    number = multiprocessing.Value('i', 0)

    lock = multiprocessing.Lock()
    
    p1 = multiprocessing.Process(target=increment, args=(number, lock))
    p2 = multiprocessing.Process(target=increment, args=(number, lock))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(number.value)

'''
Q: What is the purpose of using a lock in the multiprocessing code snippet?
A:The purpose of using a lock in the multiprocessing code snippet is to prevent race conditions 
when multiple processes are trying to access and modify a shared resource (in this case, the `number` variable).
 By using a lock, only one process can increment the value of `number` at a time, ensuring that the increments are 
 done safely and correctly. This prevents data corruption and ensures that the final value of 
 `number` reflects the total number of increments made by both processes.
'''