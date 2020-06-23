#!/usr/bin/env python3

from math import ceil, log, floor


class CreditCalculator:

    def __init__(self):
        self.periods = 0
        self.annuity = 0
        self.principal = 0
        self.nominal_interest = 0

    def monthly_payments(self):
        credit_principal = int(input("Enter credit principal:\n"))
        monthly_payment = int(input("Enter monthly payment:\n"))
        credit_interest = float(input("Enter credit interest:\n"))

        self.nominal_interest = (credit_interest / 100) * 1 / 12
        self.periods = ceil(log(monthly_payment / (monthly_payment - (self.nominal_interest * credit_principal)), 1 + self.nominal_interest))
        years = self.periods // 12
        months = self.periods % 12

        if self.periods < 12:
            print(f"You need {months} month{'s' if self.periods % 12 > 1 else ''} to repay this credit!")
        elif self.periods >= 12 and months == 0:
            print(f"You need {years} year{'s' if self.periods >= 24 else ''} to repay this credit!")
        else:
            print(f"You need {years} year{'s' if self.periods >= 24 else ''} and {months} month{'s' if self.periods % 12 > 1 else ''}")

    def annuity_payment(self):
        credit_principal = int(input("Enter credit principal:\n"))
        periods = int(input("Enter count of periods:\n"))
        credit_interest = float(input("Enter credit interest:\n"))

        self.nominal_interest = (credit_interest / 100) * 1 / 12
        self.annuity = ceil(credit_principal * (self.nominal_interest * (1 + self.nominal_interest) ** periods) / ((1 + self.nominal_interest) ** periods - 1))

        print(f"Your annuity payment = {self.annuity}!")

    def credit_principal(self):
        monthly_payment = float(input("Enter monthly payment:\n"))
        periods = int(input("Enter monthly payment:\n"))
        credit_interest = float(input("Enter credit interest:\n"))

        self.nominal_interest = (credit_interest / 100) * 1 / 12
        self.principal = floor(monthly_payment / ((self.nominal_interest * (1 + self.nominal_interest) ** periods) / ((1 + self.nominal_interest) ** periods - 1)))

        print(f"Your credit principal = {self.principal}!")

    def menu(self):
        print("What do you want to calculate?")
        print('type "n" - for count of months,')
        print('type "a" - for annuity monthly payment,')
        print('type "p" - for credit principal:')
        choice = input()
        if choice == "n":
            self.monthly_payments()
        elif choice == "a":
            self.annuity_payment()
        elif choice == "p":
            self.credit_principal()


calc = CreditCalculator()
calc.menu()
