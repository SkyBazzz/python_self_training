import sys


def generator(last_value):
    for number in range(last_value):
        yield number


gen = generator(1000000)
lst = [i for i in range(1000000)]
print(type(gen))
print(f"{gen}")

for i in gen:
    print(f"Number is {i}")

print(sys.getsizeof(gen))
print(sys.getsizeof(lst))
next(gen)
