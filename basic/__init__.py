import functools


def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__.upper().center(20, "="))
        return func(*args, **kwargs)

    return wrapper
