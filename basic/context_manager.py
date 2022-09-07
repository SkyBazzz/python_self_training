from contextlib import contextmanager


class File:
    def __init__(self, filename: str, method: str):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        print(exc_type, exc_val, exc_tb)
        self.file.close()


with File("resources/context_manager.txt", "w") as f:
    print("Working")
    f.write("Context manager")


@contextmanager
def open_file(filename: str, method: str):
    print("enter")
    with open(filename, method) as file:
        yield file
    print("exit")


with open_file("resources/decorator_context_manager.txt", "w") as f:
    print("writing")
    f.write("decorator context manager")
