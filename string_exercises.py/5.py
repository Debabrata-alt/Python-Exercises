# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

str = input("Enter a string: ") # abc | string | ab
new_str = ""
if len(str) >= 3:
  if str.endswith("ing"):
    new_str = str + "ly"
  else:
    new_str = str + "ing"
else:
  new_str = str

print(new_str) # abcing | stringly |ab