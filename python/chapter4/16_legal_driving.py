"""
Prompt user age and display message indicating if legally allowed to drive
Output should be single statement
"""
import sys

try:
	age = int(input("What is your age? "))
except:
	sys.exit("Age must be integer.")

print("You are " + str('' if age > 15 else 'not ') + "old enough to legally drive.")

