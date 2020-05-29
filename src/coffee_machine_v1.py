#!/usr/bin/env python3
# Amount of water, milk, and coffee beans required for a cup of coffee
WATER, MILK, COFFEE = (200, 50, 15)

# Enter the available amount of water, milk, and coffee beans
water_check = int(input("Write how many ml of water the coffee machine has: "))
milk_check = int(input("Write how many ml of milk the coffee machine has: "))
coffee_check = int(input("Write how many grams of coffee beans the machine has: "))
cups = int(input("Write how many cups of coffee you will need: "))

# Calculate the amount of water, milk, and coffee beans
water_amount = water_check // WATER
milk_amount = milk_check // MILK
coffee_amount = coffee_check // COFFEE

# Maximum cups that the coffee machine can make
max_cup = min([water_amount, milk_amount, coffee_amount])

if max_cup == cups:
    print("Yes, I can make that amount of coffee")
elif max_cup > cups:
    print(f"Yes, I can make that amount of coffee {max_cup - cups} and even excess more than that")
elif max_cup < cups:
    print(f"No, I can only {max_cup} cups of coffee")

