"""
Prompt user for price and quantity of three items
Calculate subtotal, tax amount (at 5.5%), and total
"""
import sys
import functools

price1 = input("Enter the price of item 1: ")
quant1 = input("Enter the quantity of item 1: ")
price2 = input("Enter the price of item 2: ")
quant2 = input("Enter the quantity of item 2: ")
price3 = input("Enter the price of item 3: ")
quant3 = input("Enter the quantity of item 3: ")

try:
	price1 = float(price1)
	price2 = float(price2)
	price3 = float(price3)
	price1 = int(price1*100)
	price2 = int(price2*100)
	price3 = int(price3*100)
except:
	sys.exit("Prices should be numeric.")

try:
	quant1 = int(quant1)
	quant2 = int(quant2)
	qunat3 = int(quant3)
except:
	sys.exit("Quantities should be integers.")

subtotal = sum(map(lambda x, y: x*y, [price1, price2, price3], [quant1, quant2, quant3]))

