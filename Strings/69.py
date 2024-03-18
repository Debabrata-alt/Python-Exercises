# 108. Write a Python program that takes a string and returns # on both sides of each element, which are not vowels.
# Sample Data:
# ("Green" -> "-G--r-ee-n-"
# ("White") -> "-W--h-i-t-e"
# ("aeiou") -> "aeiou"


def func(string):
  new_string = ""
  for el in string:
    if el not in "AEIOUaeiou":
      new_string += "-"+el+"-"
    else:
      new_string += el
  return new_string


print(func("Green")) # -G--r-ee-n-
print(func("White")) # -W--h-i-t-e
print(func("aeiou")) # aeiou