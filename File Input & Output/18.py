# Write a Python program to extract characters from various text files and puts them into a list.

import string, os

if not os.path.exists("letters"):
  os.makedirs("letters")
  
for letter in string.ascii_uppercase:
  with open(letter + ".txt", "w") as f:
    f.writelines(letter)