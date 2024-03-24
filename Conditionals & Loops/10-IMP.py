# Write a Python program to check the validity of passwords input by users.
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smalls = "abcdefghijklmnopqrstuvwxyz"
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chars = ["$", "#", "@"]

def myFunc():
  password = input("Enter a password: ")
  return password

def validation(password):
  if len([char for char in password if char in caps]) == 0:
    print("Password should have at least one uppercase letter")
    
    password = myFunc()
    validation(password)
    
  elif len([char for char in password if char in smalls]) == 0:
    print("Password should have at least one lowercase letter")
    
    password = myFunc()
    validation(password)
    
  elif len([char for char in password if char in nums]) == 0:
    print("Password should have at least one number 1 - 9")
    
    password = myFunc()
    validation(password)
    
  elif len([char for char in password if char in chars]) == 0:
    print("Password should have at least one character - $, # or @")
    
    password = myFunc()
    validation(password)
    
  elif len(password) < 6:
    print("Password should have mininum 6 characters")
    
    password = myFunc()
    validation(password)
    
  elif len(password) > 16:
    print("Password length should not exceed 16 characters")
    
    password = myFunc()
    validation(password)
  
  return f"Password = {password}"


password = myFunc()

print(validation(password))


#/////////////////////////////////////////////////////////////////////////////////////////

# Import the 're' module for regular expressions
import re

p = input("Input your password: ")

# Set 'x' to True to enter the while loop
x = True

# Start a while loop that continues until 'x' is True
while x:  
    # Password length should be between 6 and 12 characters
    if (len(p) < 6 or len(p) > 12):
        break
    # Password should contain at least one lowercase letter
    elif not re.search("[a-z]", p):
        break
    # Password should contain at least one digit
    elif not re.search("[0-9]", p):
        break
    # Password should contain at least one uppercase letter
    elif not re.search("[A-Z]", p):
        break
    # Password should contain at least one special character among '$', '#', '@'
    elif not re.search("[$#@]", p):
        break
    # Password should not contain any whitespace character
    elif re.search("\s", p):
        break
    else:
        # If all conditions are met, print "Valid Password" and set 'x' to False to exit the loop
        print("Valid Password")
        x = False
        break

# If 'x' remains True, print "Not a Valid Password"
if x:
  print("Not a Valid Password")

#///////////////////////////////////////////////////////////////////////////////////////////

# What is "\s" in python?

# n Python, the escape sequence \s matches any whitespace character. This includes spaces, tabs, newlines, and carriage returns.
# Escape sequences are used to represent special characters in Python strings. For example, the escape sequence \n represents a newline character, and the escape sequence \t represents a tab character.

#///////////////////////////////////////////////

# Match any whitespace character: 

import re

string = "This is a string with whitespace."

match = re.search("\s", string)

if match:
    print("Match found at index:", match.start())

# Match found at index: 4

#////////////////////////////////////////////////////////////////////////////////////////////

# NOTE: 

l = len([])
print(l) # 0