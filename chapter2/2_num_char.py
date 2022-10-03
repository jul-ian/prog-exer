# Prompt user for string
# Display string and number of characters in string

user_input = ''
while not user_input:
	user_input = input('What is the input string? ')
	if len(user_input) > 0:
		print(f'{user_input} has {len(user_input)} characters.')
	else:
		print('User must enter something into the program.')


