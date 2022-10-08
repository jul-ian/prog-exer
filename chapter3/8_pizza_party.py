"""
Prompt user for number of people and number of pizzas
Print summary, number of slices each person gets, number of leftovers
"""

import sys

num_ppl = input("How many people? ")
num_piz = input("How many pizzas do you have? ")

try:
	num_ppl = int(num_ppl)
	num_piz = int(num_piz)
except:
	sys.exit("Number of people and pizza must both be integers.")

slice_per_pizza = 8
total_slices = slice_per_pizza * num_piz
slices_per_person = int(total_slices / num_ppl)
leftovers= total_slices % num_ppl

if slices_per_person > 1:
	piece = 'pieces'
else:
	piece = 'piece'

print(f"{num_ppl} people with {num_piz} pizzas")
print(f"Each person gets {slices_per_person} {piece} of pizza.")
print(f"There are {leftovers} leftover pieces of pizza.")

