# Switch only python 3.10 and above

#direction = input("Which direction? ").lower()
direction = "north"
match direction:
    case "north":
        print("Up")
    case "south":
        print("Down")
    case "east":
        print("Right")
    case "west":
        print("Left")
    case _: #indicates no matches
        print("Not a valid direction")

# Challenge
# Create a switch for a number

import random

number = random.randint(0,56)

match number:
    case 0:
        print("Infant")
    case 2:
        print("Child")
    case 12:
        print("Teen")
    case 17:
        print("Adult")
    case 55: 
        print("Senior")
    case _:
        print("Not a valid age")