#!/usr/bin/env python3

import random


class Hangman:
    def __init__(self):
        """This is a constructor"""
        self.word = ['python', 'java', 'kotlin', 'javascript']
        self.welcome = "H A N G M A N"
        self.random_word = list(random.choice(self.word))  # The randomly generated word
        self.letters_remaining = "-" * (len(self.random_word))  # The randomly generated word as a hint, replaced with dashes
        self.lives = 8

    def replay(self):
        prompt = input('Type "play" to play the game, "exit" to quit: ')
        if prompt == "play":
            self.start()
        elif prompt == "exit": 
            exit()
    
    def start(self):
        """Starts the game"""
        print(self.welcome)
        self.guesser()

    def win(self):
        """Win message"""
        print("You guessed the word!")
        print("You survived!")
        self.replay()

    def lose(self):
        """Lose message"""
        print(f"The word was " + ("".join(map(str, self.random_word))) + "!")
        print("You are hanged!")
        self.replay()

    def guesser(self):
        """This is the main game logic"""
        word = list(self.letters_remaining)  # Created a new word list() for hints
        tries = []
        print()
        print(self.letters_remaining)
        while True:  # Loop for 8 attempts
            if word == self.random_word:  # Condition to check the the choice word matches the random word
                self.win()
                break
            choice = input("Input a letter: ")
            if len(choice) != 1:
                print("You should input a single letter")
            elif not choice.islower() or choice.isdigit(): 
                print("It is not an ASCII lowercase letter")
            elif choice in word:
                tries.append(choice)
                print("You already typed this letter")
            elif choice in tries:
                tries.append(choice)
                print("You already typed this letter")
            elif self.lives == 1:  # Lost conditions
                if choice in word:
                    print("You already typed this letter")
                    self.lose()
                    break
                else:
                    if choice in tries:
                        print("You already typed this letter")
                        self.lose()
                        break
                    elif len(choice) != 1:
                        print("You should input a single letter")
                        self.lose()
                        break
                    elif not choice.islower() or choice.isdigit(): 
                        print("It is not an ASCII lowercase letter")
                        self.lose()
                        break
                    print("No such letter in the word")
                    self.lose()
                    break
            elif choice in self.random_word:  # Checks if the choice matches the generated word
                for letter in range(0, len(self.random_word)):  # Iterate over the letters of the generated word
                    if choice == self.random_word[letter]:  # Match the choice with random letter of the generated word
                        word[letter] = choice  # Use the word list() for hints to and update it while matching the user choice
            elif choice not in word:  # If the letter is not in the word print the statement below
                self.lives -= 1
                tries.append(choice)
                print(f"Life: {self.lives}")
                print("No such letter in the word")


            print()
            print(*word, sep="")  # Unpacks the iterable list and removes the spaces


new_game = Hangman()
new_game.replay()
