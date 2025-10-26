import random
import time 

print("Hi, welcome to the guessing game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Too low, guess higher! What is your guess?: "))
    else:
        guess = int(input("Too high, guess lower! What is your guess?: "))
        
print(f"Congrats! You got the right answer! The number is {correct_number}. It took you {guess_count} guesses.")
