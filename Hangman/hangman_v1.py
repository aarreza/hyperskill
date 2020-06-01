#!/usr/bin/env python3

class Hangman:
    def __init__(self):
        self.word = "python"
        self.welcome = "H A N G M A N"

    def start(self):
        print(self.welcome)
        choice = input("Guess the word: > ")
        if choice != self.word:
            print("You are hanged!")
        else:
            print("You survived!")


new_game = Hangman()
new_game.start()
