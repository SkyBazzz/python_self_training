from string import ascii_lowercase
from collections import defaultdict
from random import sample


def letters_count():
    dictionary = {}
    accuracy = 0
    with open("resources/story", "r", encoding="UTF8") as story:
        for line in story:
            formatted_line = line.lower()
            accuracy += formatted_line.count("python")
            count_letters(dictionary, formatted_line)

    print(f"Word Python (ignore case) was presented {accuracy} time(s).")
    most_freq_letter = max(dictionary.keys(), key=lambda x: dictionary.get(x))
    print(
        f"Most frequently used letter is {most_freq_letter} - {dictionary[most_freq_letter]} time(s)."
    )
    print(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))


def count_letters(dictionary, line):
    for letter in ascii_lowercase:
        if line.count(letter) == 0:
            continue
        dictionary[letter] = dictionary.get(letter, 0) + line.count(letter)


def test_default_dic():
    dict = defaultdict(str)
    dict["key"] = "value"
    print(iter(dict).__next__())
    print(dict[1])
    print(dict[3])


def random_something():
    print(sample(range(1, 10), 3))


if __name__ == "__main__":
    letters_count()
