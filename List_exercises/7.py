# Write a Python function that takes two lists and returns True if they have at least one common member.

def func(list1, list2):
  return len([el for el in list1 if el in list2]) >= 1


print(func([1, 2, 3, 4, 5], [5, 6, 7, 8, 9])) # True

print(func([1, 2, 3, 4, 5], [6, 7, 8, 9])) # False