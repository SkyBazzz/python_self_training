from typing import Callable, Any


def decorator_function_with_args(first, second, third):
    print("Before decoration")

    def wrap(function):
        print("Inside wrap()")

        def wrapped_f(*args, **kwargs):
            print("Inside wrapped_f()")
            print("Decorator arguments:", first, second, third)
            result = function(*args, **kwargs)
            print(result)
            print("After f(*args)")

        return wrapped_f

    print("After decoration")
    return wrap


@decorator_function_with_args("hello", "world", 42)
def say_hello(first_arg, second_arg, third_arg, forth_arg):
    print("sayHello arguments:", first_arg, second_arg, third_arg, forth_arg)


print("After decoration1")

say_hello("say", "hello", "argument", "list")
print("after second sayHello() call")


def tracer(function):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"call {wrapper.count} to {function.__name__}")
        return function(*args, **kwargs)

    wrapper.count = 0

    return wrapper


@tracer
def printer(first_arg, second_arg):
    print(f"{first_arg!s} {second_arg!r}")


printer(1, 2)
printer(4, 3)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def give_raise(self, percent):
        self.pay *= 1.0 + percent

    @tracer
    def last_name(self):
        return self.name.split()[-1]


bob = Person("Bon", 1000)
bob.give_raise(0.1)
bob.give_raise(0.1)
bob.give_raise(0.1)


def decorator_with_args(decorator_to_enhance: Callable[[Callable, Any, Any], None]):
    print(1)
    print("Starting decorator with args")

    def decorator_maker(*args, **kwargs):
        print(3)

        print("Making decorator")

        def decorator_wrapper(func: Callable[[Any, Any], None]):
            print(5)

            print("Decorator wrapper")
            return decorator_to_enhance(func, *args, **kwargs)

        print(4)

        return decorator_wrapper

    print(2)

    return decorator_maker


@decorator_with_args
def decorated_decorator(func: Callable[[Any, Any], None], *args, **kwargs):
    print(6)

    print("In decorated decorator")

    def wrapper(func_args1: int, func_args2: int):
        print(8)
        print(f"I have received {func_args1=} and {func_args2=}")
        print(*args)
        print(**kwargs)
        return func(func_args1, func_args2)

    print(7)

    return wrapper


@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1: int, function_arg2: int):
    print(9)
    print("Hello", function_arg1, function_arg2)


# one line
# decorator_with_args(decorated_decorator)(42, 404, 1024)(decorated_function)(32, 43)

decorated_function(32, 43)


def method_friendly_decorator(method_to_decorate):
    def wrapper(*args):
        self, some = args
        lie = some - 3
        return method_to_decorate(self, lie)

    return wrapper


class Lucy:
    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def say_your_age(self, lie: int) -> None:
        print(f"I am {self.age + lie}, What do you think, how old am I?")


l = Lucy()
l.say_your_age(-3)
