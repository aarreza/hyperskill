#!/usr/bin/env python3
class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def menu(self):
        self.choice = input("Write action (buy, fill, take, remaining, exit): ")
        if self.choice == "buy":
            self.buy()
        elif self.choice == "fill":
            self.fill()
        elif self.choice == "take":
            print("")
            print(f"I gave you ${self.money}")
            print("")
            self.money -= self.money
            self.menu()
        elif self.choice == "remaining":
            self.remaining()
        elif self.choice == "exit":
            exit()
        else:
            print("")
            self.menu()
        return self.menu()

    def buy(self):
        self.choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if self.choice == "1":
            self.espresso()
        elif self.choice == "2":
            self.latte()
        elif self.choice == "3":
            self.cappuccino()
        elif self.choice == "back":
            print("")
        return self.menu()

    def espresso(self):
        if self.water >= 250 and self.beans >= 16:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
        elif self.water < 250:
            print("Sorry not enough water!")
        elif self.beans < 16:
            print("Sorry not enough beans!")
        elif self.cups < 1:
            print("Sorry not enough cups!")
        print("")
        self.menu()

    def latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
        elif self.water < 350:
            print("Sorry not enough water!")
        elif self.milk < 75:
            print("Sorry not enough milk!")
        elif self.beans < 20:
            print("Sorry not enough beans!")
        elif self.cups < 1:
            print("Sorry not enough cups!")
        print("")
        return self.menu()

    def cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
            print("")
        elif self.water < 200:
            print("Sorry not enough water!")
        elif self.milk < 100:
            print("Sorry not enough milk!")
        elif self.beans < 12:
            print("Sorry not enough beans!")
        elif self.cups < 1:
            print("Sorry not enough cups!")
        print("")
        return self.menu()

    def fill(self):
        print("")
        self.add_water = int(input("Write how many ml of water do you want to add: "))
        self.water += self.add_water
        self.add_milk = int(input("Write how many ml of milk do you want to add: "))
        self.milk += self.add_milk
        self.add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
        self.beans += self.add_beans
        self.add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.cups += self.add_cups
        print("")
        return self.menu()

    def remaining(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")
        print("")
        return self.menu()


coffee_machine = CoffeeMachine()
coffee_machine.menu()

