import os


def draw(number: int):
    if number <= 0:
        return
    draw(number - 1)

    print("#" * number, end="")
    print("")


def factorial(number):
    if number <= 2:
        return number
    return number * factorial(number - 1)


def fibonacci(number):
    return number if number <= 1 else fibonacci(number - 1) + fibonacci(number - 2)


def print_directory_tree(path, indent=""):
    print(f"{indent}+-- {os.path.basename(path)}/")
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        try:
            if os.path.isdir(item_path):
                print_directory_tree(item_path, f"{indent}    ")
            else:
                print(f"{indent}    +-- {item}")
        except PermissionError:
            print(f"{indent}+-- {os.path.basename(path)}/ - no permissions")


if __name__ == "__main__":
    draw(4)
    print(fibonacci(5))
    print_directory_tree("/Users/obalkash/PycharmProjects/python_self_training")
