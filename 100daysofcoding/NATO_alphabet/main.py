import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_letters = {value.letter: value.code for (index, value) in data.iterrows()}

user_word = input("Enter a word: ").upper()
print([nato_letters[letter] for letter in user_word])
