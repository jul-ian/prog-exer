"""
Not sure how this program is supposed to be created, specifications are kind of hazy. I'll try it though.
Prompt user for username and password, then "I don't know you" if not correct, or "Welcome!" if correct.
Will make up user and passwords for it. Will use random username and password generator.
"""
import getpass

user_pass = {"alanA": "1234", "jamesL": "jl55jl", "kateB": "randomstuff11", "mrX": "999word999"}

username = input("Username: ")
password = getpass.getpass()

if password == user_pass.get(username, 0):
	print("Welcome!")
else:
	print("I don't know you.")

