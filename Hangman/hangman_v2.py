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
        choice = input("Guess the word: > ")
        r = random.choice(self.word)
        print(r)
        if choice == r:
            print("You survived!")
        else:
            print("You are hanged!")


new_game = Hangman()
new_game.start()

