# Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

from random import randint

def myFunc():
  random_no = randint(1, 10)
  user_choice = int(input("Enter a number between 1 and 10: "))
  if user_choice == random_no:
    print("Well guessed!")
  else: 
    print("Not matched!")
    myFunc()

# execute the function
myFunc()

#/////////////////////////////////////////////////////////////////////////////////////////

import random

target_num, guess_num = random.randint(1, 10), 0

while target_num != guess_num:
  guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))

print('Well guessed!') 
