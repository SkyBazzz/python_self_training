import argparse


def main(user_name: str, user_age: int):
    print(f"Your name is {user_name}")
    print(f"Your age is {user_age}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Person name")
    parser.add_argument("-a", "--age", help="Person age")
    args = parser.parse_known_args()[0]
    name = args.name
    age = args.age
    main(name, age)
