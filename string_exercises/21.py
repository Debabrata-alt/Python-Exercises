#  Write a Python program to check whether a string starts with specified characters.

def check_chars(s):
  return s.startswith("www")


print(check_chars("www.google.com")) # True
print(check_chars("google.www.com")) # False