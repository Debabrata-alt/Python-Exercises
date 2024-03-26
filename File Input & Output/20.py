# Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.

import string

def myFunc(n):
  with open("demo8.txt", mode="w") as f:
    alphabet = string.ascii_uppercase
    letters = [alphabet[i: i + n] + "\n" for i in range(0, len(alphabet), n)]
    f.writelines(letters)

# execute the function
myFunc(3)

#/////////////////////////////////////////////////////////////////////////
# NOTE: 

uppercases = string.ascii_uppercase

lowercases = string.ascii_lowercase

all_letters = string.ascii_letters

print(uppercases) 
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(lowercases)
# abcdefghijklmnopqrstuvwxyz

print(all_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

