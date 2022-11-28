"""
Create program to help user troubleshoot car issues using given decision tree
"""

# This is probably the worst exercise in the book so far

ans1 = input("Is the car silent when you turn the key? ")

if ans1.lower() == 'y':
	ans2 = input("Are the battery terminals corroded? ")
	if ans2.lower() == 'y':
		print("Clean terminals and try starting again.")
	else:
		print("Replace cables and try again.")
else:
	ans2 = input("Does the car make a clicking noise? ")
	if ans2.lower() == 'y':
		print("Replace the battery.")
	else:
		ans3 = input("Does the car crank up but fail to start? ")
		if ans3.lower() == 'y':
			print("Check the spark plug connections.")
		else:
			ans4 = input("Does the engine start and then die? ")
			# This branch does not have an option for "no" in the diagram
			if ans4.lower() == 'y':
				ans5 = input("Does your car have fuel injection? ")
				if ans5 == 'y':
					print("Get it in for service.")
				else:
					print("Check to ensure the choke is opening and closing.")

