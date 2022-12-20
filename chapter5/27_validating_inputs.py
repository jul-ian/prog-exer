"""
Write a program that prompts for a first name, last name,
employee ID, and ZIP code. Ensure that the input is valid
according to these rules:
- The first name must be filled in.
- The last name must be filled in.
- The first and last names must be at least two characters
long.
- An employee ID is in the format AA-1234. So, two let-
ters, a hyphen, and four numbers.
- The ZIP code must be a number.
Display appropriate error messages on incorrect data.
"""

def is_filled_in(string):
	return len(string) > 0

def is_long_enough(string):
	return len(string) > 1

def is_employee_id(string):
	if len(string) != 7:
		return False
	else:
		string1 = string[:2]
		string2 = string[2]
		string3 = string[3:]
		return (string1.isalpha()) and (string2 == '-') and (string3.isdigit())

def is_zip_numeric(string):
	return string.isdigit()

def validate_input(first_name, last_name, zip_code, id):
	if not is_filled_in(first_name):
		first_name_status = "The first name should be filled in."
	elif not is_long_enough(first_name):
		first_name_status = f'"{first_name}" is not a valid first name. It is too short.'
	else:
		first_name_status = ""

	if not is_filled_in(last_name):
		last_name_status = "The last name should be filled in."
	elif not is_long_enough(last_name):
		last_name_status = f'"{last_name}" is not a valid last name. It is too short.'
	else:
		last_name_status = ""

	if not is_zip_numeric(zip_code):
		zip_status = "The ZIP code must be numeric."
	else:
		zip_status = ""

	if not is_employee_id(id):
		id_status = f'"{id}" is not a valid ID.'
	else:
		id_status = ""

	return (first_name_status, last_name_status, zip_status, id_status)

def newline(string):
	return '' if string == '' else '\n'

first = input("Enter the first name: ")
last = input("Enter the last name: ")
zip = input("Enter ZIP code: ")
id = input("Enter an employee ID: ")

fval, lval, zval, ival = validate_input(first, last, zip, id)

if (fval + lval + zval + ival == ""):
	print("There were no errors found.")

else:
	print(f"{fval}{newline(fval)}{lval}{newline(lval)}{zval}{newline(zval)}{ival}")
