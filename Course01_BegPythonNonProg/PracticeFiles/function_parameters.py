#Parameters are a way to pass info into a function
#e.g. pass in new name to hello function

def hello(name):
    print(f"Hello {name}!")

hello("Kelly")

#pass in multiple parameters
def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(4, 8)

#Challenge:
#Create a function called dog_info that takes in a dog's name & age and prints a sentence about that dog

def dog_info(name, age):
    print(f"The dog's name is {name} and they are {age} years old")

dog_info('Lucy', 12)