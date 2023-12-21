"""
Prompt user for current age and age would like to retire
Print strings indicating age, year  when able to retire
If age negative, indicate already able to retire
"""
import sys
from datetime import datetime

cur_age = input("What is your age? ")
ret_age = input("At what age would you like to retire? ")

try:
	cur_age = int(cur_age)
	ret_age = int(ret_age)
except:
	sys.exit("Both inputted ages should be integers.")

if ret_age <= cur_age:
	sys.exit("You can already retire.")
else:
	print(f"You have {ret_age - cur_age} years until you can retire.")
	print(f"It's {datetime.now().year}, so you can retire in {datetime.now().year + (ret_age - cur_age)}.")


