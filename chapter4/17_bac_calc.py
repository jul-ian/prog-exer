"""
Prompt user for your weight, gender, number of drinks, 
the amount of alcohol by volume of the drinks consumed, 
and the amount of time since last drink.
Calculate BAC using formula BAC = (A × 5.14 / W × r) − .015 × H, where
A is total alcohol consumed, in ounces (oz)
W is body weight in pounds
r is the alcohol distribution ratio: 0.73 for men, 0.66 for women
H is number of hours since the last drink
Display BAC and message indicating if legal to drink
"""
import sys

try:
	weight = float(input("Enter weight in pounds: "))
	drinks = int(input("Enter number of drinks: "))
	alc_percent = float(input("Enter the percentage of alcohol in drinks: "))
	time = float(input("Enter the number of hours since last drink: "))
except:
	sys.exit("All inputs except gender must be numeric.")

gender = input("Enter gender (M/F): ")

# Will use lower of the ratios for female or if anything else is entered
alc_dist_ratio = 0.73 if gender.lower() == 'm' else 0.66

al_p = alc_percent if 0 < alc_percent < 1 else alc_percent/100

# Will assume 12 ounces per drink
bac = (((12 * drinks * al_p) * 5.14) / (weight * alc_dist_ratio)) - (0.015 * time)

print(f'Your BAC is {bac:.5f}')
print(f'It is {"" if bac < 0.08 else "not "}legal for you to drive.')





