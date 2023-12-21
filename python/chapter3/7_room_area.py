"""
Prompt user for length and width of room in feet
Print area of room in feet and meters squared
"""

import sys

length = input("What is the length of the room in feet? ")
width = input("What is the width of the room in feet? ")

try:
	length = float(length)
	width = float(width)
except:
	sys.exit("Both length and width must be numeric.")

conv_const = 0.09290304

squ_feet = length*width
squ_meter = squ_feet*conv_const

if int(squ_feet) == squ_feet:
	squ_feet = int(squ_feet)
if int(squ_meter) == squ_meter:
	squ_meter = int(squ_meter)

print(f"You entered dimensions of {length} by {width} feet.")
print(f"The area is\n{squ_feet} square feet\n{squ_meter:.3f} square meters")

