# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


def last_item(n):
  return n[-1]


def func(list):
  return sorted(list, key = last_item)


sorted_list = func([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])

print(sorted_list) # [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]