"""
Prompt for the amount of principal, rate of interest (as percentage), and number of years
Print amount principal is worth growing at simple interest at rate of interest for number of years
"""
import sys

try:
	principal = float(input("Enter the principal: "))
	interest = float(input("Enter the interest: "))
	years = float(input("Enter the number of years: "))
except:
	sys.exit("All entered values must be numeric.")

str_years = "years" if years > 1 else "year"
years = int(years) if int(years) == years else years

print(f"After {years} {str_years} at {interest}%, the investment will be worth ${principal * (1 + years * (interest / 100)):.2f}")

