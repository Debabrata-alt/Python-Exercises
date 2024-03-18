# Write a Python program to find the list of words that are longer than n from a given list of words.

def func(string, n):
  list1 = string.split()
  return [el for el in list1 if len(el)> n]


print(func("The quick brown fox jumps over the lazy dog", 3))
# ['quick', 'brown', 'jumps', 'over', 'lazy']