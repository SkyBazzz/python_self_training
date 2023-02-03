def decorator_function_with_arguments(arg1, arg2, arg3):
    print("Before decoration")

    def wrap(f):
        print("Inside wrap()")

        def wrapped_f(*args, **kwargs):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            result = f(*args, **kwargs)
            print(result)
            print("After f(*args)")

        return wrapped_f

    print("After decoration")
    return wrap


@decorator_function_with_arguments("hello", "world", 42)
def say_hello(a1, a2, a3, a4):
    print("sayHello arguments:", a1, a2, a3, a4)


print("After decoration1")

say_hello("say", "hello", "argument", "list")
print("after second sayHello() call")


def tracer(f):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"call {wrapper.count} to {f.__name__}")
        return f(*args, **kwargs)

    wrapper.count = 0

    return wrapper


@tracer
def printer(a, b):
    print(f"{a!s} {b!r}")


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


def decorator_with_args(decorator_to_enhance):
    print(1)
    print("Starting decorator with args")

    def decorator_maker(*args, **kwargs):
        print(3)

        print("Making decorator")

        def decorator_wrapper(func):
            print(5)

            print("Decorator wrapper")
            return decorator_to_enhance(func, *args, **kwargs)

        print(4)

        return decorator_wrapper

    print(2)

    return decorator_maker


@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    print(6)

    print("In decorated decorator")

    def wrapper(func_args1, func_args2):
        print(8)
        print(f"I have received {func_args1=} and {func_args2=}")
        print(*args)
        print(**kwargs)
        return func(func_args1, func_args2)

    print(7)

    return wrapper


# decorated_decorator = decorator_with_args(decorated_decorator)


@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print(9)
    print("Hello", function_arg1, function_arg2)


# decorated_function = decorated_decorator(42, 404, 1024)(decorated_function)

decorated_function(32, 43)


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3
        return method_to_decorate(self, lie)

    return wrapper


# class Lucy(object):
#
#     def __init__(self):
#         self.age = 32
#
#     @method_friendly_decorator
#     def say_your_age(self, lie):
#         print(f"I am {self.age + lie}, What do you think, how old am I?")
#
#
# l = Lucy()
# l.say_your_age(-3)
