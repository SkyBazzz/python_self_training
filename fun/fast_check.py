# Python program to explain the
# use of wait() method in Event() class
import enum
from enum import Enum
from itertools import permutations
import os

I = 1111


def helper_function(event_obj, timeout, i):
    # Thread has started, but it will wait 10 seconds for the event
    print("Thread started, for the event to set")

    flag = event_obj.wait(timeout)
    if flag:
        print("Event was set to true() earlier, moving ahead with the thread")
    else:
        print("Time out occured, event internal flag still false. Executing thread without waiting for event")
        print("Value to be printed=", i)


class Numbers(Enum):
    FIRST = enum.auto()
    SECOND = enum.auto()
    THIRD = enum.auto()


if __name__ == '__main__':
    # # Initialising an event object
    # event_obj = threading.Event()
    #
    # # starting the thread who will wait for the event
    # thread1 = threading.Thread(target=helper_function, args=(event_obj, 4, 27))
    # thread1.start()
    # # sleeping the current thread for 5 seconds
    # time.sleep(5)
    #
    # # generating the event
    # event_obj.set()
    # print("Event is set to true. Now threads can be released.\n")
    # print()
    # tuple of vowels

    # def some_test(start):
    #     def nested(label):
    #         print(label, nested.state)
    #         nested.state += 1
    #
    #     nested.state = start
    #     return nested
    #
    #
    # f = some_test(10)
    # f('some')
    # print(f.state)
    # f('haha')
    # print(f.state)

    # numbers = tuple(map(lambda number: number.value + 3, Numbers))
    # [print(number) for number in numbers]
    #
    # catalogue = ['a', 'b', 'c', 'd']
    # result = ''.join(catalogue)
    # print(result)

    ...


# def some_func(*, d):
#     print(d)
#
#
# some_func(d=3)
#
# catalogue1 = [lambda n: rt ** n for rt in range(1, 6)]
# catalogue2 = [lambda n, rt=rt: rt ** n for rt in range(1, 6)]
#
# for value in range(1, 5):
#     print(catalogue1[value](2), catalogue2[value](2))
#
#
# def heh(a, b, c):
#     print(((a and b) or c))
#
#
# heh(1, 2, 3)


# Sentinel value
# blocks = []
# for block in iter(input, ''):
#     blocks.append(block)
#
# print(blocks)
# graduation_date = namedtuple("GraduationDate", ("year", "month"))
#
# def graduation():
#     return graduation_date(2011, 8)
#
# print(graduation())

def tracer(f):
    def wrapper(*args):
        wrapper.count += 1
        print(f'call {wrapper.count} to {f.__name__}')
        return f(*args)

    wrapper.count = 0

    return wrapper


@tracer
def printer(a, b):
    print(f"{a!s} {b!r}")


printer(1, 2)
printer(4, 3)

new = type("New", (object,), dict(a="sobaka", b="cat"))
type(new)

max_workers = min(32, (os.cpu_count() or 1) + 4)
print(os.cpu_count())
print(max_workers)
[print(perm) for perm in permutations(["Sobaka", "Sobaka2", "Sobaka3", "Sobaka4"], 3)]

print(f"Comparison files:downloaded file from FCnF({new}) and " f"uploaded one")
