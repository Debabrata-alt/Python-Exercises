# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def func(myStr):
  myList = myStr.split("-")
  return "-".join(sorted(myList))

print(func("green-red-yellow-black-white"))
# black-green-red-white-yellow