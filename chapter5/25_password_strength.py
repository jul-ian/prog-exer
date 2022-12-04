"""
Prompt user for password

Determine password strength according to following rules:
- A very weak password contains only numbers and is
fewer than eight characters.
- A weak password contains only letters and is fewer than
eight characters.
- A strong password contains letters and at least one
number and is at least eight characters.
- A very strong password contains letters, numbers, and
special characters and is at least eight characters.
These conditions were indicated in the book, 
but a password with less than 8 characters with a mix of letters and numbers is not included.
Will classify this type of password as weak
Also passwords with 8 or more characters that are all characters or numbers will be classified as weak

Print message indicating password strength
"""
import re
def passwordValidator(password):
	"""
	Function to determine strength of password
	Returns integer code defined as follows:
		1 - Very Weak
		2 - Weak
		3 - Strong
		4 - Very Strong
	"""
	if len(password) < 8:
		# Is either very weak or weak password
		if re.sub(r'[0-9]', '', password) == "":
			return 1
		else:
			return 2
	else:
		# Is either strong or very strong password, unless has only one type of character
		contains_letter = re.search(r'[a-zA-Z]', password)
		contains_number = re.search(r'[0-9]', password)
		contains_special_chr = re.search(r'[^0-9a-zA-Z]', password)
		if bool(contains_letter and contains_number and contains_special_chr):
			return 4
		elif bool(contains_letter and contains_number):
			return 3
		else:
			return 2

password = input("Enter password: ")
password_strength = passwordValidator(password)
if password_strength == 1:
	strength = 'very weak'
elif password_strength == 2:
	strength = 'weak'
elif password_strength == 3:
	strength = 'strong'
else:
	strength = 'very strong'

print(f"The password '{password}' is a {strength} password.")

