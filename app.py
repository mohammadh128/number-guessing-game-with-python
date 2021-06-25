# importing the libraries
import random
import math


# intro section
print("""hello!!!
this is a guessing game.
please enter your bound for the game to start""")


# getting the inputs
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# generating the random number between the chosen bound
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

# Initializing the number of guesses.
guess_count = 0

# while loop for each round of the game
while guess_count < math.log(upper - lower + 1, 2):
    guess_count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              guess_count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
        print("You have ", round(math.log(upper - lower + 1, 2)) -
              guess_count, " guess left")
    elif x < guess:
        print("You Guessed too high!")
        print("You have ", round(math.log(upper - lower + 1, 2)) -
              guess_count, " guess left")


# If you guessed more than your chances the game will end
if guess_count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
