from memory_profiler import profile

@profile
def my_function():
    a = [i for i in range(100000)]  # Consumes memory
    b = [i * 2 for i in a]         # More memory consumption
    return b

if __name__ == "__main__":
    my_function()

'''
Q: What is the purpose of using the @profile decorator in this code?
A: The purpose of using the @profile decorator in this code is to monitor and analyze the memory 
usage of the `my_function` function. When the function is executed, the decorator tracks how much 
memory is allocated and deallocated during its execution. This allows developers to identify 
potential memory leaks or inefficiencies in their code, helping them optimize memory usage and improve 
performance. The output from the memory profiler will show the memory consumption at different 
points in the function, making it easier to pinpoint areas that may need optimization.
'''
