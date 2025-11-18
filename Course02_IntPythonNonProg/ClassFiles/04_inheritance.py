import random

class Animal:
    info = 'a living organism that feeds on organic matter'

    def __init__(self, name):
        print("An animal is created")
        self.name = name

class Dog(Animal):
    info = "a furry friend"


    def __init__(self, name):
        super().__init__(name)
        print("A dog is created")
        self.lucky_number = random.randint(1,10)
        self.fur = ""

    def bark(self):
        print(f"woof! My name is {self.name} and my number is {self.lucky_number}")


class Bulldog(Dog):
    
    def __init__(self, name):
        super().__init__(name)
        print("A Bulldog is created")

dog1 = Bulldog("Fido")


# Challenge
# In your previous class, add a parent
# or a child class

class House:
    area = 1000

    def __init__(self, area):
        print(f"The area of the house is {area}")

class Office(House):

    def __init__(self, area):
        super().__init__(area)
        print("The house has an office")

newhouse = Office(2000)