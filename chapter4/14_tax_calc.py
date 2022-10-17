"""
Prompt user for order amount and state
If state is Wisconsin, print subtotal, tax at 5.5%, and total
If any other state, print total with no tax
"""
import sys

try:
	order_amt = float(input("What is the order amount? "))
except:
	sys.exit("Order amount should be numeric.")

state = input("What is the state? ")

tax = 0.0

if state.lower() == "wi" or state.lower() == "wisconsim":
	tax = 0.055
	print(f"The subtotal is ${order_amt:.2f}.\nThe tax is ${tax * order_amt:.2f}.")

print(f"The total is ${order_amt * (1 + tax):.2f}.")
