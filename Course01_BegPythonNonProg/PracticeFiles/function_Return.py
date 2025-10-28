#Return info from a function that can be used 

def double(number):
    return number * 2

new_number = double(5)

print(new_number)

#Challenge:
#Create a function that returns a string in all caps

def caps(word):
    return word.upper()

print(caps("lucy"))


names = ['nick', 'jane', 'sara']

for name in names:
    print(caps(name))