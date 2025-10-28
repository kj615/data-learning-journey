'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
1. randomly generate two lists to test
2. Write this in one line of code (we're probably not there yet)
'''

import random

list_one = []
list_two = []

for a in range(0,100):
    list_one.append(random.randint(0,100))
for a in range(0,10):
    list_two.append(random.randint(0,100))

overlap = []

for number in list_one:
    if number in list_two:
        overlap.append(number)
    
for number in list_two:
    if number in list_one and number not in overlap:
        overlap.append(number)

print(list_one)
print(list_two)
print(overlap)
