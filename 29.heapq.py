import heapq

class TaskScheduler:
    def __init__(self):
        # Priority queue (min-heap)
        self.task_queue = []

    def add_task(self, priority, task_name):
        """
        Add a task to the priority queue.
        Priority: Lower values indicate higher priority.
        """
        heapq.heappush(self.task_queue, (priority, task_name))
        print(f"Task '{task_name}' added with priority {priority}")

    def execute_task(self):
        """
        Execute the highest-priority task.
        """
        if self.task_queue:
            priority, task_name = heapq.heappop(self.task_queue)
            print(f"Executing task '{task_name}' with priority {priority}")
        else:
            print("No tasks to execute.")

    def peek_next_task(self):
        """
        Peek at the highest-priority task without removing it.
        """
        if self.task_queue:
            priority, task_name = self.task_queue[0]
            print(f"Next task to execute: '{task_name}' with priority {priority}")
        else:
            print("No tasks in the queue.")

# Example Usage
if __name__ == "__main__":
    scheduler = TaskScheduler()

    # Add tasks
    scheduler.add_task(3, "Write report")
    scheduler.add_task(1, "Fix critical bug")
    scheduler.add_task(2, "Attend team meeting")

    # Peek at the next task
    scheduler.peek_next_task()

    # Execute tasks in order of priority
    scheduler.execute_task()
    scheduler.execute_task()
    scheduler.execute_task()

    # Try to execute with no tasks
    scheduler.execute_task()

'''
Q: What is heapq in Python? What data structure does it implement, and what are its primary use cases?
A: The `heapq` module in Python provides an implementation of the heap queue algorithm, also known as the 
priority queue algorithm. It implements a min-heap data structure, where the smallest element is always at 
the root of the heap. The primary use cases for `heapq` include implementing priority queues, 
finding the n largest or n smallest elements in a dataset, and maintaining a collection of items with 
associated priorities.

Q: What are the time complexities of the primary operations provided by the `heapq` module, such as `heappush`, 
`heappop`, and `heapify`?
A: The time complexities of the primary operations provided by the `heapq` module are as follows:
- `heappush(heap, item)`: O(log n), where n is the number
    of elements in the heap. This operation adds a new item to the heap while maintaining the heap property.
- `heappop(heap)`: O(log n), where n is the number of elements in the heap. This operation removes and
    returns the smallest item from the heap while maintaining the heap property.
- `heapify(x)`: O(n), where n is the number of elements in the list x. This operation transforms a list into a
    heap in-place, in linear time.

Q: How can you tranform heapq into a max-heap, given that it is implemented as a min-heap by default?
A: To transform `heapq` into a max-heap, you can invert the priority of the elements by storing the 
negative of the values. This way, the smallest (most negative) value will represent the highest 
priority in the max-heap.
'''
