#!/usr/bin/env python3

import random


class Hangman:
    def __init__(self):
        self.word = ['python', 'java', 'kotlin', 'javascript']
        self.welcome = "H A N G M A N"

    def start(self):
        print(self.welcome)
        self.guesser()

    def guesser(self):
        r = random.choice(self.word)
        chosen_word = r[0:3]
        remaining_letters = "-" * (len(r) - 3)
        choice = input(f"Guess the word {chosen_word}{remaining_letters}: ")
        if choice == r:
            print("You survived!")
            print(f"Correct, the word {r}!")
        else:
            print("You are hanged!")
            print(f"Wrong, the word is {r}!")


new_game = Hangman()
new_game.start()
