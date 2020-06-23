#!/usr/bin/env python3

from math import ceil

credit_principal = int(input("Enter the credit principal:\n"))
calc = input("""What do you want to calculate? 
type "m" - for count of months,
type "p" - for monthly payment:\n""")
if calc == "m":
    monthly_pay = int(input("Enter monthly payment:\n"))
    mp_calc = round(credit_principal / monthly_pay)
    print()
    if mp_calc > 1:
        print(f"It takes {mp_calc} months to repay the credit")
    else:
        print(f"It takes {mp_calc} month to repay the credit")
elif calc == "p":
    months = int(input("Enter count of months:\n"))
    payment = ceil(credit_principal / months)
    last_payment = credit_principal - (months - 1) * payment
    print()
    if last_payment != payment:
        print(f"Your monthly payment = {payment} with last month payment = {last_payment}.")
    else:
        print(f"Your monthly payment = {payment}")
