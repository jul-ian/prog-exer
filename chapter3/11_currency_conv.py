"""
Prompt user for number of euros exchanging to dollars and exchange rate
Print number of euros, exchange rate, number of dollars
"""

import sys
import math

try:
	euros = float(input("How many euros are you exchanging? "))
	euros = int(euros * 100)
	rate = float(input("What is the exchange rate? "))
except:
	sys.exit("Number of euros and exchange rate must be numeric.")

dollars = math.ceil(euros * rate) / 100
euros = euros / 100

print(f"{euros:.2f} euros at an exchange rate of {rate} is {dollars:.2f} U.S. dollars.")


