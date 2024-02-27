# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

str = input("Enter the string: ") # w3resource | w3 | w
new_str = ""
if len(str) < 2:
  new_str = ""
else:
  new_str += str[0] + str[1] + str[-2] + str[-1]

print(new_str) # w3ce | w3w3 | (empty string)