# Guess game
import random
Jackpot = random.randint(1,20)

guess = int(input("Enter your number:"))
counter = 1
while guess != Jackpot:
    if guess < Jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guess = int(input("Enter your number:"))
    counter+=1
print("correct answer")
print("you took",counter,"attempts")