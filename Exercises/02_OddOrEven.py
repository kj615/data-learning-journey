'''
Ask the user for a number.
Depending on whether the number is even or odd, print an appropriate message to the user.

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different message.
'''

number = int(input("Provide a  number: "))

if number % 2 == 0 and number % 4 != 0:
    print('Your number is even')
elif number % 4 == 0:
    print('Your number is divisible by 4')
else:
    print('Your number is odd')



num = int(input("Provide a number: "))
check = int(input("Provide another number: "))

if num % check == 0:
    print("Your numbers divide evenly")
else:
    print("Your numbers don't divide evenly")
