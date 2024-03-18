# Write a Python program to check whether a string contains all letters of the alphabet.

#//////////////////////////////////////////////////////////////////////////

# Import the 'string' module to access all uppercase and lowercase letters (alphabet)
import string

# Create a set 'alphabet' containing all uppercase and lowercase letters using 'string.ascii_letters'.
alphabet = set(string.ascii_letters)

def check_string(string):
  return all(s in alphabet for s in string)

print(check_string("The quick brown fox jumps over the lazy dog")) # True

print(check_string("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")) # True
print(check_string("ABCDEFGHIJ KLMNOPQRSTUVWXYZ abcdefghijklmn opqrstuvwxyz")) # True

print(check_string("I am Raju")) # True


#/////////////////////////////////////////////////////////////////////////////

# Import the 'string' module to access the lowercase alphabet
import string

# Create a set 'alphabet' containing all lowercase letters using 'string.ascii_lowercase'
alphabet = set(string.ascii_lowercase)

# Define an input string
input_string = "The quick brown fox jumps over the lazy dog"

# Check if the set of lowercase characters in the input string contains all the letters of the alphabet.
# Print the result (True or False).
print(set(input_string.lower()) >= alphabet) # True

# Update the input string.
input_string = "The quick brown fox jumps over the lazy cat"

# Check if the set of lowercase characters in the updated input string contains all the letters of the alphabet.
# Print the result (True or False).
print(set(input_string.lower()) >= alphabet) # False