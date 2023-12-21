"""
Prompt user for 5 numbers
Print total of five numbers to user
Ignore any attempts that are not numbers
"""

numlist = []
for _ in range(5):
    try:
        num = float(input("Enter a number: "))
        numlist.append(num)
    except:
        continue

total = sum(numlist)
if total == int(total):
    print(f"The total is {total:.0f}.")
else:
    print(f"The total is {total}.")
