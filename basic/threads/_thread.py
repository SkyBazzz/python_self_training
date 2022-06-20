# Write your code here.
import threading

number = int(input("Enter a positive integer: "))


def print_text_n_times(n):
    [print("foobar", end="") for _ in range(1, n)]


thread1 = threading.Thread(target=print_text_n_times, args=(number,))
thread2 = threading.Thread(target=print_text_n_times, args=(number,))

thread1.start()
thread2.start()
