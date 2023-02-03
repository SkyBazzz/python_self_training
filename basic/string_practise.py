# Case fold
from datetime import datetime
from dateutil.parser import parse
import pickle
import sys
import re

from basic import log_function


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
        print(f"MyClass __format__ called with {format_spec=!r}")
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


@log_function
def bytes_practise():
    byte_string = b"spam"
    string_string = "eggs"
    print((byte_string[0], string_string[0]))
    print((byte_string[1:], string_string[1:]))
    print(list(byte_string), list(string_string))
    print(string_string.encode())
    print(bytes(string_string, encoding="ascii"))
    print(byte_string.decode())
    print(str(byte_string, encoding="utf-16"))
    print(str(byte_string, encoding="ascii"))
    print(sys.platform)
    print(sys.getdefaultencoding())
    print(len(str(byte_string)))
    print(len(str(byte_string, encoding="utf-8")))

    byte_string = "AÄBèC"
    print(byte_string.encode("cp500"), "IBM EBCDIC")
    print(byte_string.encode("latin-1"))
    print(byte_string.encode("utf-8"))
    print(byte_string.encode("cp850"))
    byte_string = "spam"  # ASCII text
    print("ASCII text the same in most but not EBCDIC encoding")
    print(byte_string.encode("cp500"), "in IBM EBCDIC")
    print(byte_string.encode("latin-1"), "in latin-1")
    print(byte_string.encode("utf-8"), "in utf-8")
    print(byte_string.encode("cp850"), "in cp850")


@log_function
def re_string_practise():
    str_text = "Bugger all down here on earth!"
    byte_text = b"Bugger all down here on earth!"
    print(re.match("(.*) down (.*) on (.*)", str_text).groups())
    print(re.match(b"(.*) down (.*) on (.*)", byte_text).groups())
    print(pickle.dumps([1, 2, 3], protocol=0))
    pickle.dump([1, 2, 3], open("re_pickle", "wb"), protocol=0)
    print(pickle.load(open("re_pickle", "rb"), encoding="ascii"))


# equals_debugging()
# conversions()
# formatting()
# bytes_practise()
# re_string_practise()
text = "hello world"
print(text.partition(" "))
log_row = "INFO 2020-10-15T03:05:15PM some information"
timestamp = parse(log_row, fuzzy_with_tokens=True)
print(timestamp)
