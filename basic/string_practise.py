# Case fold
from datetime import datetime


def compare_greek():
    upper = "Σ"
    lower = "σ"
    final_pos = "ς"

    print(upper == lower)
    print(upper == final_pos)
    print(final_pos == lower)
    print("===============")
    upper_cf = upper.casefold()
    lower_cf = lower.casefold()
    final_pos_cf = final_pos.casefold()
    print(upper_cf)
    print(lower_cf)
    print(final_pos_cf)
    print("===============")
    print(upper_cf == lower)
    print(upper_cf == final_pos_cf)
    print(final_pos_cf == lower)


# f string

def equals_debugging():
    str_value = "other 🐶"
    num_value = 123
    print(f'The value is {str_value}')
    print(f'{str_value=}')
    print(f'{num_value % 2 = }')


def conversions():
    str_value = "other 🐶"
    print(f"{str_value!a}")
    print(f"{str_value!r}")
    print(f"{repr(str_value)}")


class MyClass:
    def __format__(self, format_spec: str) -> str:
        print(f'MyClass __format_ called with {format_spec=!r}')
        return "MyClass()"


def formatting():
    num_value = 123.456
    now = datetime.utcnow()
    print(f'{now=:%Y-%m-%d}')
    print(f'{num_value=:.2f}')
    print(f'{MyClass()=:blah blah %%MYFORMAT%%}')

    nested_format = '.2f'
    print(f'{num_value:{nested_format}}')
equals_debugging()
conversions()
formatting()
