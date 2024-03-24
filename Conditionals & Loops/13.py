# Write a Python program to check whether an alphabet is a vowel or consonant.
# Expected Output:

# Input a letter of the alphabet: k                                       
# k is a consonant.

def myFunc(char):
  if char in "aeiou":
    print(f"{char} is a vowel")
  else:
    print(f"{char} is a consonant")

myFunc("k")
# k is a consonant
myFunc("e")
# e is a vowel