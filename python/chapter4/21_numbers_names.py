"""
Prompt user for number of month
Print message giving name of month
"""
import sys

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
try:
	num = int(input("Please enter the number of the month: "))
except:
	sys.exit("Number of the month must be an integer.")

try:
	month = months[num - 1]
except:
	sys.exit("Number of month must be between 1 and 12.")

print(f"The name of the month is {month}.")

