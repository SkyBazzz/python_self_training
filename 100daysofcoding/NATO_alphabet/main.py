import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_letters = {value.letter: value.code for (index, value) in data.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        output_list = ([nato_letters[letter] for letter in user_word])
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
