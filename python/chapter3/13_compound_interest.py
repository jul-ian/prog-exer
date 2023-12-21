"""
Prompt for the amount of principal, rate of interest (as percentage), number of years, and compounding frequency
Print amount principal is worth growing at compuound interest
"""
import sys

try:
	principal = float(input("Enter the principal: "))
	interest = float(input("Enter the interest: "))
	years = float(input("Enter the number of years: "))
	compound = int(input("What is the number of times the interest is compounded per year? "))
except:
	sys.exit("All entered values must be numeric.")

str_years = "years" if years > 1 else "year"
years = int(years) if int(years) == years else years
amount = principal * (1 + (interest / 100) / compound) ** (compound * years)

print(f"${principal:.2f} invested at {interest}% for {years} {str_years} compounded {compound} times per year is ${amount:.2f}")

