#'''You're given a list of ints called numbers
# Task: find the even numbers and add them all together
# Return the sum of all evens
# Expected result: 392'''
    
numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]
total = 0

for num in numbers:
    if num % 2 == 0:
        total = total + num

print(total)
