# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


def func(list):
  count = 0
  for el in list:
    if len(el) >=2 and el[0] == el[-1]:
      count += 1
  return count

print(func(['abc', 'xyz', 'aba', '1221'])) # 2