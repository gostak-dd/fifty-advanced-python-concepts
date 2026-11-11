# py -3.14t -X gil=1 .\55.without_gil.py (time taken: ~7.13secs)
# py -3.14t -X gil=0 .\55.without_gil.py (time taken: ~2.6secs)

"""
Important:
    This module requires the Python 3.13+ free-threaded build to execute 
    agents concurrently. Run this script using `py -3.14t .\55.without_gil.py` or 
    ensure `PYTHON_GIL=0` is set in your environment.
"""

import sys
import threading
import time

def compute_heavy(n):
    total = 0
    for i in range(n):
        total += i
    return total

def execute_workers(num_threads, workload):
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=compute_heavy, args=(workload,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    print(f"GIL active: {sys._is_gil_enabled()}")
    
    start = time.perf_counter()
    execute_workers(4, 50_000_000)
    end = time.perf_counter()
    
    print(f"Execution time: {end - start:.4f}s")