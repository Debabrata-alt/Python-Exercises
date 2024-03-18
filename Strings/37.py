# Write a Python program to lowercase the first n characters in a string.

def func(string, n):
  return string[:n].lower() + string[n:]


print(func("W3RESOURCE.COM", 4)) # w3reSOURCE.COM