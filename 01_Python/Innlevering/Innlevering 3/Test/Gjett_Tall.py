# Innlevering 3
import random as ra
llimit = int(input("Enter lower limit: "))
ulimit = int(input("Enter upper limit: "))

rando = ra.randint(llimit, ulimit)
guess = int()
while (guess != rando):
    guess = int(input("Guess a number: "))
    if (guess > rando):
        print("Your guess is a bit high, try again")
    elif (guess < rando):
        print("Your guess is a bit low, try again")
    else:
        print("Correct! The answer was {0}".format(rando))
