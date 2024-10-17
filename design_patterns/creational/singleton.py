"""
The Singleton Pattern restricts the instantiation of a class to a single instance
and provides a global point of access to that instance.
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(singleton1 is singleton2)  # True
