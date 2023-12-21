"""
Prompt user for height in inches and weight in pounds
Print message stating bmi and if in ideal weight range
If not in ideal weight range, print message to consult doctor and whether under or overweight
"""

import sys

try:
	height = float(input("Enter height in inches: "))
	weight = float(input("Enter weight in inches: "))
except:
	sys.exit("Values entered for height and weight must both be numeric.")

bmi = (weight / height**2) * 703

if 18.5 <= bmi <= 25:
	bmi_msg = "You are within the ideal weight range."
elif bmi < 18.5:
	bmi_msg = "You are underweight. You should see your doctor."
elif bmi > 25:
	bmi_msg = "You are overweight. You should see your doctor."

print(f"Your BMI is {bmi:.1f}.\n{bmi_msg}")
