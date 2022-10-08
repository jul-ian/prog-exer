"""
Prompt the user for 2 number
Print the sum, difference, product, and quotient
"""
import sys

num1 = input("What is the first number? ")
num2 = input("What is the second number? ")

try:
	num1 = int(num1)
	num2 = int(num2)
except:
	sys.exit("Both inputs must be numbers.")

if(num1 < 0 or num2 < 0):
	sys.exit("Both numbers must be nonnegative.")

quot = num1 / num2
if int(quot) == quot:
	quot = int(quot)

print(f"{num1} + {num2} = {num1 + num2}\n{num1} - {num2} = {num1-num2}\n{num1} * {num2} = {num1*num2}\n{num1} / {num2} = {quot}")
