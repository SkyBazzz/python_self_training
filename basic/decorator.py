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
        print(f'call {wrapper.count} to {f.__name__}')
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
        self.pay *= (1.0 + percent)

    @tracer
    def last_name(self):
        return self.name.split()[-1]


bob = Person("Bon", 1000)
bob.give_raise(0.1)
bob.give_raise(0.1)
bob.give_raise(0.1)
