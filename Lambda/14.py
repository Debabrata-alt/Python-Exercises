# Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
# Sample Output:
# Monday
# Friday
# Sunday

myList = weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

val = list(filter(lambda el: len(el) == 6, myList))

for v in val:
  print(v)
  
  # Monday
  # Friday
  # Sunday