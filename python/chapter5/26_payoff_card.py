"""
Prompt user for balance, APR as percent, monthly payment user will make
Print message indicating how many months it will take to pay off card
"""

import sys
import math

try:
	balance = float(input("What is your balance? "))
	apr = float(input("What is the APR on the card (as a percent)? ")) / 100
	payment = float(input("What is the monthly payment you can make? "))
except:
	sys.exit("Inputs must be numeric.")

def payoff_months(balance, apr, payment):
	n_months = (-1/30) * math.log(1 + (balance/payment) * (1 - (1 + apr/365)**30)) / math.log(1 + apr/365)
	return n_months

months_payoff = int(math.ceil(payoff_months(balance, apr, payment)))

print(f"It will take you {months_payoff} months to pay off this card.")
