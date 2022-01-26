from typing import Any


class Meta(type):
    def __new__(mcs, class_name: str, bases: tuple, attrs: dict):
        replaced = {}

        for name, value in attrs.items():
            if name.startswith("__"):
                replaced[name] = value
            else:
                replaced[name.upper()] = value

        return type(class_name, bases, replaced)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print(f"{self} - 'barks hi'")


d = Dog()
d.HELLO()  # it works thing we've changed the case of the attribute hello to be in upper case
d.hello()  # doesn't work anymore. Dog do not have attribute hello (starts with lower case)
