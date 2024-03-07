# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def func(list):
  return [el for (i, el) in enumerate(list) if i not in (0, 4, 5)]


print(func(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
# ['Green', 'White', 'Black']