"""
Prompt user for two strings
Check if they are anagrams and print message that includes strings
 notifying user if they are anagrams
Will ignore spaces, case, and punctuation when determining if anagram
"""
import re

print("Enter two strings and I'll tell you if they are anagrams:")
first = input("Enter the first string: ")
second = input("Enter the second string: ")

def isAnagram(str1, str2):
	regexp = re.compile(r"[^a-z0-9]")

	str1 = regexp.sub("", str1.lower())
	str2 = regexp.sub("", str2.lower())

	if len(str1) != len(str2):
		return False
	if ''.join(sorted(str1)) == ''.join(sorted(str2)):
		return True
	else:
		return False

is_anagram = isAnagram(first, second)

is_or_not = "" if is_anagram else "not "

print(f'"{first}" and "{second}" are {is_or_not}anagrams.')

