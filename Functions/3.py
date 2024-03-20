# Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

myStr = "The quick Brow Fox"

def func(myStr):
  len_up = len([el for el in myStr if el.isupper()])
  len_lo = len([el for el in myStr if el.islower()])
  return len_up, len_lo


print(func(myStr))
# (3, 12)