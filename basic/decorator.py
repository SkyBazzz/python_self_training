def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")

        def wrapped_f(*args, **kwargs):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args, **kwargs)
            print("After f(*args)")

        return wrapped_f

    return wrap


@decorator_function_with_arguments("hello", "world", 42)
def say_hello(a1, a2, a3, a4):
    print("sayHello arguments:", a1, a2, a3, a4)


print("After decoration")

say_hello("say", "hello", "argument", "list")
print("after second sayHello() call")
