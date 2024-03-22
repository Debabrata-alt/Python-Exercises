# Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
# Input the string: W3resource
# ['Valid string.']

def isValid(myStr):
  message = [
    # String must have 1 upper case character
    lambda new_string: any(el.isupper() for el in new_string),
    # String must have 1 lower case character
    lambda new_string: any(el.islower() for el in new_string),
    # String must have 1 number
    lambda new_string: any(el.isdigit() for el in new_string),
    # String length should be at least 8
    lambda new_string: len(new_string) >= 8
  ]
  
  result = [e for e in [el(myStr) for el in message] if e != True]
  
  # if 'result' list is empty
  if not result:
    return "It is a valid string"
  else:
    return "Not a valid string"


print(isValid("W3resource"))
# It is a valid string