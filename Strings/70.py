# 108. Write a Python program that takes a string and returns # on both sides of each element, which are not vowels.
# Sample Data:
# ("Green" -> "-G--r-ee-n-"
# ("White") -> "-W--h-i-t-e"
# ("aeiou") -> "aeiou"


def func(text):
  return "".join([el, '-' + el + '-'][el not in "AEIOUaeiou"] for el in text)


print(func("Green")) # -G--r-ee-n-
print(func("White")) # -W--h-i-t-e
print(func("aeiou")) # aeiou