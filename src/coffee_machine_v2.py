#!/usr/bin/env python3
# Initial stock of the coffee machine
water, milk, beans, disposable_cups, money = (400, 540, 120, 9, 550)


def initial_stock():
    """This function will display the current stock"""
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")


def buy_action():
    """This function will buy coffee"""
    choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    # Calculate espresso
    espresso_water = water - 250
    espresso_milk = milk - 0
    espresso_beans = beans - 16
    espresso_cups = disposable_cups - 1
    espresso_cost = money + 4

    # Calculate latte
    latte_water = water - 350
    latte_milk = milk - 75
    latte_beans = beans - 20
    latte_cups = disposable_cups - 1
    latte_cost = money + 7

    # Calculate cappuccino
    cap_water = water - 200
    cap_milk = milk - 100
    cap_beans = beans - 12
    cap_cups = disposable_cups - 1
    cap_cost = money + 6

    # Display the current stock
    if choice == "1":
        print("\nThe coffee machine has: ")
        print(f"{espresso_water} of water")
        print(f"{espresso_milk} of milk")
        print(f"{espresso_beans} of coffee beans")
        print(f"{espresso_cups} of disposable cups")
        print(f"{espresso_cost} of money")
    elif choice == "2":
        print("\nThe coffee machine has: ")
        print(f"{latte_water} of water")
        print(f"{latte_milk} of milk")
        print(f"{latte_beans} of coffee beans")
        print(f"{latte_cups} of disposable cups")
        print(f"{latte_cost} of money")
    elif choice == "3":
        print("\nThe coffee machine has: ")
        print(f"{cap_water} of water")
        print(f"{cap_milk} of milk")
        print(f"{cap_beans} of coffee beans")
        print(f"{cap_cups} of disposable cups")
        print(f"{cap_cost} of money")


def fill_action():
    """This function will stock the coffee machine"""
    # Additional amount
    add_water = int(input("Write how many ml of water do you want to add: "))
    add_milk = int(input("Write how many ml of milk do you want to add: "))
    add_beans = int(input("Write how many grams of coffee beans do you want to add: "))
    add_cups = int(input("Write how many disposable cups of coffee do you want to add: "))

    # Calculate stock after filling
    fill_water = water + add_water
    fill_milk = milk + add_milk
    fill_beans = beans + add_beans
    fill_cups = disposable_cups + add_cups
    fill_money = money

    # Display the current stock
    print("\nThe coffee machine has:")
    print(f"{fill_water} of water")
    print(f"{fill_milk} of milk")
    print(f"{fill_beans} of coffee beans")
    print(f"{fill_cups} of disposable cups")
    print(f"{fill_money} of money")


def take_action():
    """This function will take money from the coffee machine"""
    # Calculate money withdrawn

    money_taken = money - money

    # Display remaining money
    print("\nThe coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money_taken} of money")


def machine_main():
    if action == "buy":
        buy_action()
    elif action == "fill":
        fill_action()
    elif action == "take":
        take_action()


initial_stock()
action = input("\nWrite action (buy, fill, take): ")
machine_main()
