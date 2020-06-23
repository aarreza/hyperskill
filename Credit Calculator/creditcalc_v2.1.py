from math import ceil, log, floor

class CreditCalculator:

    def __init__(self):
        self.periods = 0
        self.annuity = 0
        self.credit_principal = 0
        self.nominal_interest = 0
        self.monthly_payment = 0
        self.interest = 0
        self.choice = ''

    def calc_monthly_payment(self):
        self.periods = ceil(log(self.monthly_payment / (self.monthly_payment - (self.nominal_interest * self.credit_principal)), 1 + self.nominal_interest))
        years = self.periods // 12
        months = self.periods % 12

        if self.periods < 12:
            print(f"You need {months} month{'s' if self.periods % 12 > 1 else ''} to repay this credit!")
        elif self.periods >= 12 and months == 0:
            print(f"You need {years} year{'s' if self.periods >= 24 else ''} to repay this credit!")
        else:
            print(f"You need {years} year{'s' if self.periods >= 24 else ''} and {months} month{'s' if self.periods % 12 > 1 else ''}")

    def calc_annuity_payment(self):
        self.annuity = ceil(self.credit_principal * (self.nominal_interest * (1 + self.nominal_interest) ** self.periods) / ((1 + self.nominal_interest) ** self.periods - 1))
        
        print(f"Your annuity payment = {self.annuity}!")
        
    def calc_credit_principal(self):
        self.credit_principal = floor(self.monthly_payment / ((self.nominal_interest * (1 + self.nominal_interest) ** self.periods) / ((1 + self.nominal_interest) ** self.periods - 1)))
        
        print(f"Your credit principal = {self.credit_principal}!")

    def calc_nominal_interest(self):
        self.nominal_interest = (self.interest / 100) * 1 / 12

    def menu(self):
        print("What do you want to calculate?")
        print('type "n" - for count of months,')
        print('type "a" - for annuity monthly payment,')
        print('type "p" - for credit principal:')
        self.choice = input()
        if self.choice != 'p':
            print("Enter credit principal:")
            self.credit_principal = float(input())
        if self.choice != 'a':
            print("Enter monthly payment:")
            self.monthly_payment = float(input())
        if self.choice != 'n':
            print("Enter count of periods:")
            self.periods = float(input())
        print("Enter credit interest:")
        self.interest = float(input())
        self.calc_nominal_interest()

        if self.choice == 'n':
            self.calc_monthly_payment()
        elif self.choice == 'a':
            self.calc_annuity_payment()
        elif self.choice == 'p':
            self.calc_credit_principal()


calc = CreditCalculator()
calc.menu()