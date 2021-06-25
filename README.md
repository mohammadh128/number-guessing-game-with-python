# number-guessing-game-with-python
Number guessing game in Python

---------------------------------
step 1:
  user selects a range

---------------------------------
step 2:
  using the choosen bounds we select a random number between the given bounds
  
---------------------------------
step 3:
  let's say the user select a range from lower_bound to upper_bound.
  then we create a number of chances for the user to guess the number using the following formula:
  number_of_guesses = log2(upper_bound – lower_bound + 1)
  
---------------------------------
step 4:
  create a while so that the user can guess multiple times.
  
---------------------------------
step 5:
  If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You Guessed too high!“
  Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You Guessed too small!”
  And if the user guessed in a minimum number of guesses, the user gets a “Congratulations you did it” Output.
  Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.
