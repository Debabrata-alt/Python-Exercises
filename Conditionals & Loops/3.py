# Write a Python program that accepts a word from the user and reverses it.

user_choice = input("Enter a word: ") # Raja

def myFunc(user_choice):
  return "".join(reversed(user_choice))

print(myFunc(user_choice)) # ajaR

#/////////////////////////////////////////////////////////////////////////////////////////

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char])

