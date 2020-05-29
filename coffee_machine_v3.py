#!/usr/bin/env python3
# Initial stock of the coffee machine
current_stock = [400, 540, 120, 9, 550]


def buy_action():
    """This function will buy coffee"""
    choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    if choice == "1":
        while True:  # Checks if the coffee machine has enough stock for an espresso
            if current_stock[0] < 250:
                print("Sorry, not enough water!\n")
                break
            if current_stock[1] <= 0:
                print("Sorry not enough milk!\n")
                break
            if current_stock[2] < 16:
                print("Sorry not enough beans!\n")
                break
            if current_stock[3] <= 0:
                print("Sorry not enough cups!\n")
                break
            else:
                print("I have enough resources, making you a coffee!\n")
                current_stock[0] -= 250
                current_stock[1] -= 0
                current_stock[2] -= 16
                current_stock[3] -= 1
                current_stock[4] += 4
                break
    elif choice == "2":
        while True: # Checks if the coffee machine has enough stock for a latte
            if current_stock[0] < 350:
                print("Sorry, not enough water!\n")
                break
            if current_stock[1] <= 75:
                print("Sorry not enough milk!\n")
                break
            if current_stock[2] < 20:
                print("Sorry not enough beans!\n")
                break
            if current_stock[3] <= 0:
                print("Sorry not enough cups!\n")
                break
            else:
                print("I have enough resources, making you a coffee!\n")
                current_stock[0] -= 350
                current_stock[1] -= 75
                current_stock[2] -= 20
                current_stock[3] -= 1
                current_stock[4] += 7
                break
    elif choice == "3":
        while True: # Checks if the coffee machine has enough stock for an cappuccino
            if current_stock[0] < 200:
                print("Sorry, not enough water!\n")
                break
            if current_stock[1] <= 100:
                print("Sorry not enough milk!\n")
                break
            if current_stock[2] < 12:
                print("Sorry not enough beans!\n")
                break
            if current_stock[3] <= 0:
                print("Sorry not enough cups!\n")
                break
            else:
                print("I have enough resources, making you a coffee!\n")
                current_stock[0] -= 200
                current_stock[1] -= 100
                current_stock[2] -= 12
                current_stock[3] -= 1
                current_stock[4] += 6
                break

    elif choice == "back":
        return


def fill_action():
    """This function will stock the coffee machine"""
    # Input additional amount
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    print("")

    # Updates the current stock (list)
    current_stock[0] += add_water
    current_stock[1] += add_milk
    current_stock[2] += add_beans
    current_stock[3] += add_cups
    current_stock[4] = current_stock[4]


def take_action():
    """This function will take money from the coffee machine"""
    print('I gave you ${4}'.format(*current_stock))
    print("")
    current_stock[4] -= current_stock[4]  # Calculate money withdrawn and updates


def remaining_action():
    """This function displays the remaining amount of stock"""
    print("The coffee machine has:")
    print('{0} of water'.format(*current_stock))
    print('{1} of milk'.format(*current_stock))
    print('{2} of beans'.format(*current_stock))
    print('{3} of disposable cups'.format(*current_stock))
    print('${4} of money'.format(*current_stock))
    print("")


x = ""
while True:
    x = input("Write action (buy, fill, take, remaining, exit): ")
    if x == "exit":
        break
    else:
        if x == "buy":
            buy_action()
        elif x == "fill":
            fill_action()
        elif x == "take":
            take_action()
        elif x == "remaining":
            remaining_action()
