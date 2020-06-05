#!/usr/bin/env python3

import random


class Hangman:
    def __init__(self):
        """This is a constructor"""
        self.word = ['python', 'java', 'kotlin', 'javascript']
        self.welcome = "H A N G M A N"
        self.random_word = list(random.choice(self.word))  # The randomly generated word
        self.letters_remaining = "-" * (len(self.random_word))  # The randomly generated word as a hint, replaced with dashes
        self.lives = 8 # Initiate the number of lives

    def start(self):
        """Starts the game"""
        print(self.welcome)
        self.guesser()

    def win(self):
        """Win message"""
        print("You guessed the word!")
        print("You survived!")

    def lose(self):
        """Lose message"""
        print(f"The word was " + ("".join(map(str, self.random_word))) + "!")
        print("You are hanged!")

    def guesser(self):
        """This is the main game logic"""
        word = list(self.letters_remaining)  # Created a new word list() for hints
        print()
        print(self.letters_remaining)
        while True:  # Loop for 8 attempts
            if word == self.random_word:
                self.win()
                break
            choice = input("Input a letter: ")
            if self.lives == 1:
                if choice in word:
                    print("No improvements")
                    self.lose()
                    break
                else:
                    print("No such letter in the word.")
                    self.lose()
                    break
            elif choice in word:
                self.lives -= 1
                print("No improvements")
            elif choice in self.random_word:  # Checks if the choice matches the generated word
                for letter in range(0, len(self.random_word)):  # Iterate over the letters of the generated word
                    if choice == self.random_word[letter]:  # Match the choice with random letter of the generated word
                        word[letter] = choice  # Use the word list() for hints to and update it while matching the user choice

            else:  # If the letter is not in the word print the statement below
                self.lives -= 1
                print("No such letter in the word")

            print()
            print(*word, sep="")  # Unpacks the iterable list and removes the spaces

new_game = Hangman()
new_game.start()
