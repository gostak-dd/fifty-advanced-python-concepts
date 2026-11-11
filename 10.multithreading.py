import threading
import time

def download(url):
    print(f"Starting download: {url}")
    time.sleep(2)  # Simulate download time
    print(f"Finished download: {url}")

urls = ["url1", "url2", "url3"]

threads = []

start = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All downloads completed in", time.time() - start, "seconds")


from concurrent.futures import ThreadPoolExecutor
import time

def download(url):
    print(f"Downloading: {url}")
    time.sleep(2)
    print(f"Finished: {url}")

urls = ["url1", "url2", "url3"]

start = time.time()
with ThreadPoolExecutor() as executor:
    executor.map(download, urls)
print("All downloads completed in", time.time() - start, "seconds")

'''
Q: How does multithreading improve performance in I/O-bound tasks?
A: Multithreading improves performance in I/O-bound tasks by allowing multiple threads to run concurrently.
When one thread is waiting for an I/O operation (like downloading a file) to complete,
    other threads can continue executing. This leads to better resource utilization 
    and faster overall execution time for I/O-bound tasks.
'''
