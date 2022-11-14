"""
Program to input order amount and taxes will be calculated
For Illinois, tax is 8%. For Wisconsin, 5% plus 0.005 for Eau Claire county, plus 0.004 for Dunn county. 0% for all other states.
Print message with tax amount and total for Illinois and Wisconsin, just total for all other states.
"""
import sys

try:
	amt = float(input("What is the order amount? "))
except:
	sys.exit("Order amount must be numeric.")

state = input("What state do you live in? ")
if state.lower() in ('wisconsin', 'wi'):
	tax = 0.05
	county = input("What county do you live in? ")
	if county.lower() == 'eau claire':
		tax += 0.005
	elif county.lower() == 'dunn':
		tax += 0.004
elif state.lower() in ('illinois', 'il'):
	tax = 0.08
else:
	tax = 0.0

if state.lower() in ('illinois', 'il', 'wisconsin', 'wi'):
	print(f"The tax is ${amt*tax:.2f}")
print(f"The total is ${amt*(1 + tax):.2f}")



