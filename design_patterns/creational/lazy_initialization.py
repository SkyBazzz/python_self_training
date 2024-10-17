"""
The Lazy Initialization Pattern delays the initialization of an object until it is actually needed,
which can improve performance and reduce memory usage.
"""


class ExpensiveObject:
    def __init__(self):
        print("Creating expensive object...")
        # Expensive initialization code here
        self.some_property = "some value"

    def __str__(self):
        return "ExpensiveObject"


class LazyInitializationExample:
    def __init__(self):
        self.expensive_object = None

    def get_expensive_object(self):
        if self.expensive_object is None:
            self.expensive_object = ExpensiveObject()
        return self.expensive_object


if __name__ == "__main__":
    example = LazyInitializationExample()

    # Expensive object is not created until it is requested
    print("Retrieving expensive object for the first time...")
    obj = example.get_expensive_object()

    # Expensive object already exists, so no need to create it again
    print("Retrieving expensive object for the second time...")
    obj = example.get_expensive_object()
