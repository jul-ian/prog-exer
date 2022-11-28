"""
Prompt user for 3 numbers (integers)
If all different, print message containing the max
else exit program
"""
import sys

try:
	num1 = int(input("Enter the first number: "))
	num2 = int(input("Enter the second number: "))
	num3 = int(input("Enter the third number: "))
except:
	sys.exit("Inputs must be numeric.")

if len({num1, num2, num3}) == 3:
	max = num1
	if num2 > max: max = num2
	if num3 > max: max = num3
	print(f"The largest number is {max}.")
else:
	exit()
