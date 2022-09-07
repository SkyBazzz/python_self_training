# Write your code here.
import concurrent.futures
import random
import threading
import time

number = int(input("Enter a positive integer: "))


def print_text_n_times(n, text):
    [print(text, end="") for _ in range(1, n)]


thread1 = threading.Thread(target=print_text_n_times, args=(number, "foo"))
thread2 = threading.Thread(target=print_text_n_times, args=(number, "bar"))

thread1.start()
thread2.start()
thread_pool = [thread1, thread2]
for thread in thread_pool:
    thread.join()


def some_printing(text):
    wait = random.randint(0, 5)
    print(f"we wait {wait} sec\n")
    time.sleep(wait)
    return f"text {text}"


print("Start".center(20, "="))
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(some_printing, config) for config in range(5)]
    for future in concurrent.futures.as_completed(futures):
        return_value = future.result()
        print(return_value)
print("Final".center(20, "="))
