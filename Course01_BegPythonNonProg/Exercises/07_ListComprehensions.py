'''
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python 
that takes this list a and makes a new list that has only the even elements of this list in it.
'''
# Solved in "normal" if statement
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_list = []


for num in a:
    remainder = num % 2
    if remainder == 0:
        new_list.append(num)

print(new_list)
'''

# One-liner solution:

b = [1, 2, 3, 4, 5, 6, 7, 8]

one_liner = [num for num in b if num % 2 == 0]

print(one_liner)

