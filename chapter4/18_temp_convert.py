"""
Prompt user for unit to convert to (C or F)
Prompt user for temperature and perform conversion 
Print message stating converted temperature
"""
import sys

print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")

scale = input("Your choice: ").lower()

if not scale in ('c', 'f'): sys.exit("Choice must be either C or F.")

try:
	temperature = float(input(f"Please enter the temperature in {'Celsius' if scale == 'f' else 'Fahrenheit'}: "))
except:
	sys.exit("Temperature must be a numeric value.")

if scale == 'f':
	conv = lambda t: ((9/5) * t) + 32
else:
	conv = lambda t: (t - 32) * (5/9)

print(f"The temperature in {'Celsius' if scale == 'c' else 'Fahrenheit'} is {conv(temperature):.1f}.")
