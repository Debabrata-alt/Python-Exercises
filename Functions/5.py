# Write a Python function that checks whether a passed string is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.


def func(myStr):
  newStr = myStr.replace(" ", "")
  palin_str = "".join(newStr[n] for n in range((len(newStr) - 1), -1, -1))
  return newStr == palin_str


print(func("madam")) # True
print(func("nurses run")) # True

#///////////////////////////////////////////////////////////////////////////////////////////

def func(myStr):
  newStr = myStr.replace(" ", "")
  return newStr == newStr[::-1]

print(func("madam")) # True
print(func("nurses run")) # True



