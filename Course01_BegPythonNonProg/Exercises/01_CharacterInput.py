'''
Create a program that asks the user to enter their name and age.
Print a message addressed to them that tells them the year they will turn 100.

Extras:
Add on by asking the user for another number and printing out that many copies of the previous message

Print out that many copies of the previous message on separate lines
'''

name = input("What's your name?")
age = input("What's your age?")
fav_num = int(input("What's your favorite number?"))

hundred = 100 - int(age)
year = 2025 + int(hundred)

print((f'Hello, {name}! You will turn 100 years old in {year}') * int(fav_num))


for times in range(fav_num):
    print(f'Hello, {name}! You will turn 100 years old in {year}')