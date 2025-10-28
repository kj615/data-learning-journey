'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don't know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

user_number = int(input("Please provide a number: "))
divisors = []

for number in range(1,(user_number + 1)):
    if user_number % number == 0:
        divisors.append(number)

print(f'The divisors for {user_number} are: {divisors}')