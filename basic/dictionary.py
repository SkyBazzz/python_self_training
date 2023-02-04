import pprint
from string import ascii_lowercase
import collections
from typing import Dict, List, NamedTuple


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
    print(f"Most frequently used letter is {most_freq_letter} - {dictionary[most_freq_letter]} time(s).")
    print(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))


def count_letters(dictionary, line):
    for letter in ascii_lowercase:
        if line.count(letter) == 0:
            continue
        dictionary[letter] = dictionary.get(letter, 0) + line.count(letter)


def default_dict():
    dct = collections.defaultdict(str)
    dct["key"] = "value"
    print(iter(dct).__next__())
    print(dct["key"])
    print(dct[1])
    print(dct[3])
    print(dct)


def cities_country():
    city_by_county = {
        "Kharkiv": "UA",
        "Kyiv": "UA",
        "Mariupol": "UA",
        "Ontario": "USA",
        "New York": "USA",
        "Alaska": "USA",
        "Paris": "FR",
        "Berlin": "DE",
    }

    print("First part: validate if key in a dictionary solution.")
    dct1_result: Dict[str, List] = {}
    for city, country in city_by_county.items():
        if country in dct1_result:
            dct1_result[country].append(city)
        else:
            dct1_result[country] = [city]
    for cities in dct1_result.values():
        cities.sort()
    pprint.pprint(dct1_result)

    print("Second part: default dictionary from collections module.")
    dct2_result = collections.defaultdict(list)
    for city, country in city_by_county.items():
        dct2_result[country].append(city)

    for cities in dct2_result.values():
        cities.sort()
    pprint.pprint(dct2_result)

    print("Third part: setdefault method usage.")
    dct3_result = {}
    for city, country in city_by_county.items():
        dct3_result.setdefault(country, []).append(city)

    for cities in dct3_result.values():
        cities.sort()
    pprint.pprint(dct3_result)


if __name__ == "__main__":
    # letters_count()
    # default_dict()
    # cities_country()

    class N(NamedTuple):
        id: int
        name: str

    n = N(1, "Alex")
