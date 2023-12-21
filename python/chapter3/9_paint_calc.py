"""
Prompt user for length and width of ceiling
Print number of gallons of paint needed to paint ceiling
Assume 1 gallon of paint can cover 350 sq feet
Assure inputs are entered as numeric
"""
import sys
import math

length = input("What is the length? ")
width = input("What is the width? ")

try:
	length = float(length)
	width = float(width)
except:
	sys.exit("Length and width must be numeric.")

gallon_max = 350
area = length*width
n_gal = math.ceil(area/gallon_max)
gal = "gallon" if n_gal == 1 else "gallons"

print(f"You will need to purchase {n_gal} {gal} of paint to cover {round(area, 3)} square feet.")



