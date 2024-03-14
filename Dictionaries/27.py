# Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

myDict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

for i, j in sorted(myDict.items(), key=lambda x: x[1], reverse=True)[:3]:
  print(i, j)
  
  # item4 55
  # item1 45.5
  # item3 41.3

#////////////////////////////////////////////////////////////////////////////////

myDict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

sort_list = [(key, value) for key, value in sorted(myDict.items(), reverse=True)]

# sorting based on the keys
print(sort_list)
# [('item5', 24), ('item4', 55), ('item3', 41.3), ('item2', 35), ('item1', 45.5)]

sort_list = sorted([value for value in myDict.values()], reverse=True)[:3]

for el in sort_list:
  for key, value in myDict.items():
    if el == value:
      print(key, value)
      # item4 55
      # item1 45.5
      # item3 41.3      

#////////////////////////////////////////////////////////////////////////////////