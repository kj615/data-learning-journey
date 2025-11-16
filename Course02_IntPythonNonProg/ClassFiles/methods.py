import random

class Dog:
    info = "a furry friend"

    def __init__(self, name):
        print("I'm alive!")
        self.lucky_number = random.randint(1,10)
        self.name = name

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")

dog1 = Dog("fido")
dog2 = Dog("Sarah")

dog1.bark()
dog2.bark()


# Challenge
# In your previous class, add a method
# that uses one of the instance variables

class Office:
    furniture = "couch"

    def __init__(self, color):
        self.color = color

    def paint(self):
        print(f"This office should be painted {self.color}")

print(Office.furniture)

office1 = Office("purple")

office1.paint()
