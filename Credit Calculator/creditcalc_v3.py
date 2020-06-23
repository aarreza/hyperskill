#!/usr/bin/env python3

import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('--type', help="Type of payments")
parser.add_argument('--payment', help="Monthly payment", type=float)
parser.add_argument('--principal', help="Principal payment", type=float)
parser.add_argument('--periods', help="Number of months and/or years needed to repay the credit", type=int)
parser.add_argument('--interest', help="Principal payment", type=float)

# Parse the arguments
args = parser.parse_args()

# Variable declarations
payments = args.payment
principal = args.principal
periods = args.periods
interest = args.interest

# Financial calculations declaration
nominal_interest = 0
annuity = 0
credit_principal = 0
differential = 0
number_of_payments = 0
overpayment = 0
months = 0
years = 0

# Example 1:
if args.type == 'diff' and args.principal and args.periods and args.interest:
    nominal_interest = (interest / 100) * 1 / 12
    for m in range(1, periods + 1):
        differential = ((principal / periods) + (nominal_interest * ((principal) - (principal * (m - 1) / periods))))
        result = int(math.ceil(differential))
        print("Month {0}: paid out {1}".format(m, result))
        overpayment += result
    total_op = int(overpayment - args.principal)
    print("\nOverpayment = {}".format(total_op))

# Example 2:
elif args.type == 'annuity' and args.principal and args.periods and args.interest:
    nominal_interest = (interest / 100) * 1 / 12
    annuity = int(math.ceil(principal * (nominal_interest * (1 + nominal_interest) ** periods) / ((1 + nominal_interest) ** periods - 1)))
    print("Your annuity payment = {}!".format(annuity))
    total_op = int((annuity * periods) - principal)
    print("Overpayment = {}".format(total_op))

# Example 5:
elif args.type == 'annuity' and args.payment and args.periods and args.interest:
    nominal_interest = (interest / 100) * 1 / 12
    credit_principal = int(math.floor(payments / ((nominal_interest * (1 + nominal_interest) ** periods) / ((1 + nominal_interest) ** periods - 1))))
    print("Your credit principal = {}!".format(credit_principal))
    total_op = int((payments * args.periods) - credit_principal)
    print("Overpayment = {}".format(total_op))

# Example 6:
elif args.type == 'annuity' and args.principal and args.payment and args.interest:
    nominal_interest = (interest / 100) * 1 / 12
    number_of_payments = int(math.ceil(math.log(payments / (payments - (nominal_interest * principal)), 1 + nominal_interest)))

    years = int(number_of_payments // 12)
    months = int(number_of_payments % 12)

    if number_of_payments < 12:
        print("You need {0} month{1} to repay this credit!".format(months, 's' if number_of_payments % 12 > 1 else ''))
    elif number_of_payments >= 12 and months == 0:
        print("You need {0} year{1} to repay this credit!".format(years, 's' if number_of_payments >= 24 else ''))
    else:
        print("You need {0} year{1} and {2} month{3}".format(years, 's' if number_of_payments >= 24 else '', months, 's' if number_of_payments % 12 > 1 else ''))

    total_op = int((payments * number_of_payments) - args.principal)
    print("Overpayment = {}".format(total_op))
# Incorrect parameter checks
else:
    print("Incorrect parameters")
