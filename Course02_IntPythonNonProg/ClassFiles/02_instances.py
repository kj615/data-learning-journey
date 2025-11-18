import random 

class Dog:
    info = "A furry friend"

    # function that runs whenever an object is created from the class
    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

# print(Dog.info)

# Create individual "Dog" object from Dog class
# Each object is unique/different from each other (shown in example by random number)
'''
dog1 = Dog()
dog2 = Dog()

print(dog1.lucky_number)
print(dog2.lucky_number)

dog1.name = "fido"
print(dog1.name)

print(dog2.name)
'''

namedog1 = Dog("Lucy")
namedog2 = Dog("Joey")

print(namedog1.name)
print(namedog2.name)


# Challenge
# Whatever your previous class was,
# make an instance of it and add an instance variable/attribute to it
class Office:
    furniture = "couch"

print(Office.furniture)

office1 = Office()
office1.color = "purple"

print(office1.color)