# Write your code here
import random


class Test:

    def __init__(self):
        self.test = 0


class Game:
    words = None

    def __init__(self, words=("python", "java", "kotlin", "javascript")):
        print("H A N G M A N")
        self.words = words
        self.answer = random.choice(self.words)

    def guess_word(self):
        if self.answer == input("Guess the word: > "):
            print("You survived!")
        else:
            print("You are hanged!")


game = Game()
game.guess_word()



