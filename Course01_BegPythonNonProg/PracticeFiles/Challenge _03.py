'''
Is there a remainder?
Task: Create a function named has_remainder() that takes twon ints
and divides the first number by the second number.
The function should return True if there is a remainder.
The function should return False if there is not a remainder
'''

def has_remainder(num1, num2):
    if num1 % num2 != 0:
        return True
    else:
        return False

remainder = has_remainder(5,4)
print(remainder)

test_rem = has_remainder(4,2)
print(test_rem)