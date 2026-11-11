# import asyncio

# async def greet():
#     print("Hello!")
#     await asyncio.sleep(1)  # Pause for 1 second
#     print("World!")

# asyncio.run(greet())  # Output: Hello! (pause) World!





import asyncio

async def task_1():
    print("Task 1: Start")
    await asyncio.sleep(2)
    print("Task 1: End")

async def task_2():
    print("Task 2: Start")
    await asyncio.sleep(1)
    print("Task 2: End")

async def main():
    # Run tasks concurrently
    await asyncio.gather(task_1(), task_2())

asyncio.run(main())




import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        await queue.put(f"Item {i}")
        print(f"Produced Item {i}")
    await queue.put(None)  # Signal the consumer to exit

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())

'''
Q: Explain the purpose of the asyncio.gather() function in the main() function.
A: The asyncio.gather() function is used to run multiple asynchronous tasks concurrently. In the
    main() function, it takes the producer and consumer coroutines as arguments and schedules them to run at the same time. This 
    allows both tasks to execute concurrently, enabling the producer to generate items while 
    the consumer processes them. The gather() function waits for all the provided coroutines 
    to complete before returning, ensuring that both tasks finish their execution before the program exits.

Q: Whats the difference between asyncio.sleep() and time.sleep() in the context of asynchronous programming?
A: The difference between asyncio.sleep() and time.sleep() lies in how they handle blocking in the 
context of asynchronous programming. asyncio.sleep() is a non-blocking sleep function that allows other tasks to run while it waits,
    making it suitable for use in asynchronous code. In contrast, time.sleep() is a blocking function that halts the 
    execution of the entire program for the specified duration, preventing other tasks from running.

Q: What is the difference in asyncio and threading in python (python has GIL)?
A: The difference between asyncio and threading in Python lies in their approach to concurrency and 
how they handle the Global Interpreter Lock (GIL). asyncio is based on an event loop and uses cooperative 
multitasking, allowing a single thread to manage multiple tasks by yielding control during I/O operations. 
This makes it efficient for I/O-bound tasks but not suitable for CPU-bound tasks due to the GIL. 
Threading, on the other hand, allows for true parallelism in I/O-bound tasks but is limited by 
the GIL for CPU-bound tasks, as only one thread can execute Python bytecode at a time. 
Therefore, asyncio is preferred for I/O-bound applications, while threading may be used for 
I/O-bound tasks that require parallel execution.
'''

