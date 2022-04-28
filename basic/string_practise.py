# Case fold
from datetime import datetime
import functools


def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__.upper().center(20, '='))
        return func(*args, **kwargs)
    return wrapper


@log_function
def compare_greek():
    upper = "Σ"
    lower = "σ"
    final_pos = "ς"

    print(upper == lower)
    print(upper == final_pos)
    print(final_pos == lower)

    upper_cf = upper.casefold()
    lower_cf = lower.casefold()
    final_pos_cf = final_pos.casefold()
    print(upper_cf)
    print(lower_cf)
    print(final_pos_cf)

    print(upper_cf == lower)
    print(upper_cf == final_pos_cf)
    print(final_pos_cf == lower)


# f string

@log_function
def equals_debugging():
    str_value = "other 🐶"
    num_value = 123
    print(f"The value is {str_value}")
    print(f"{str_value=}")
    print(f"{num_value % 2 = }")


@log_function
def conversions():
    str_value = "other 🐶"
    print(f"{str_value!a}")
    print(f"{str_value!r}")
    print(f"{repr(str_value)}")


@log_function
def split_max_split(string: str, max_split: int = 2):
    return string.split(maxsplit=max_split)


class MyClass:
    def __format__(self, format_spec: str) -> str:
        print(f"MyClass __format_ called with {format_spec=!r}")
        return "MyClass()"


@log_function
def formatting():
    num_value = 123.456
    now = datetime.utcnow()
    print(f"{now=:%Y-%m-%d}")
    print(f"{num_value=:.2f}")
    print(f"{MyClass()=:blah blah %%MYFORMAT%%}")

    nested_format = ".2f"
    print(f"{num_value:{nested_format}}")
    print(split_max_split("hello my name is Afdas", 6))


equals_debugging()
conversions()
formatting()
