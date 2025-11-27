age = 90
height = 120

# and
if age > 8 and height >= 135:
    print("You can ride!")

# or
if age >= 17 or height >= 160:
    print("you can ride the super ride!")

# elif (else if)
if height < 120:
    print("You can't ride any rides :(")
elif height < 135:
    print("You can ride level 1 rides")
elif height < 200:
    print("you can ride any ride")
else:
    print("too tall for all rides :(")


# challenge
# create and if statemeht with both "and" and "or"

temp = 35
wind = 9
precip = 'yes'

if temp > 40 or wind < 10 and precip == "no":
    print("weather is favorable for a walk")
else:
    print("it's best to stay indoors today")
