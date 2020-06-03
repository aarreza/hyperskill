#!/usr/bin/env python3

import random


class Hangman:
    def __init__(self):
        """This is a constructor"""
        self.word = ['python', 'java', 'kotlin', 'javascript']
        self.welcome = "H A N G M A N\n"
        self.random_word = list(random.choice(self.word))  # The randomly generated word
        self.letters_remaining = "-" * (len(self.random_word))  # The randomly generated word as a hint, replaced with hyphens

    def start(self):
        """Starts the game"""
        print(self.welcome)
        self.guesser()

    def end(self):
        """Ends the game"""
        print("\nThanks for playing!")
        print("We'll see how well you did in the next stage")

    def guesser(self):
        """This is the main game logic"""
        guesses = 0  # Counter for guesses
        word = list(self.letters_remaining)  # Created a new word list() for hints
        print(self.letters_remaining)
        while guesses < 8:  # Loop for 8 attempts
            choice = input("Input a letter: ")
            if choice in self.random_word:  # Checks if the choice matches the generated word
                print()
                for letter in range(0, len(self.random_word)):  # Iterate over the letters of the generated word
                    if self.random_word[letter] == choice:  # Match the choice with random letter of the generated word
                        word[letter] = choice  # Use the word list() for hints to and update it while matching the user choice
                letter += 1  # Iterate through the letters by 1
            else:  # If the letter is not in the word print the statement below
                print("No such letter in the word")
                print()
            guesses += 1  # Increment through the guesses by 1
            print(*word, sep="")  # Unpacks the iterable list and removes the spaces 
        self.end()  # Ends the game


new_game = Hangman()
new_game.start()

