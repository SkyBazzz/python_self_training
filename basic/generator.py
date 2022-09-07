import sys


def generator(last_value):
    # yield from range(last_value)
    for number in range(last_value):
        yield number


right_board = 1000000
gen = generator(right_board)
lst = list(range(right_board))
print(type(gen))
print(f"{gen}")

for i in gen:
    print(f"Number is {i}")

print(sys.getsizeof(gen))
print(sys.getsizeof(lst))
next(gen)
