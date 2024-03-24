# Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

def myfunc(mystr):
  letters = len([l for l in mystr if l.isalpha()])
  digits = len([l for l in mystr if l.isdigit()])
  return letters, digits

letters, digits = myfunc("Python 3.2")

print(letters) # 6
print(digits) # 2