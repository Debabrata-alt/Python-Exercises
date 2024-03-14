# Write a Python program to get the key, value and item in a dictionary.

# Create a dictionary 'dict_num' with keys and values.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Iterate through the key-value pairs in 'dict_num' using the 'enumerate' function.
# The 'enumerate' function assigns a count starting from 1 to each pair and unpacks them as (count, (key, value)).
for count, (key, value) in enumerate(dict_num.items(), 1):
  # Print the key, value, and count in a formatted table.
  print(key, '   ', value, '    ', count) 
  
  # 1     10      1
  # 2     20      2
  # 3     30      3
  # 4     40      4
  # 5     50      5
  # 6     60      6

#/////////////////////////////////////////////////////////////////////////////////////

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for index, value in enumerate(dict_num.items()):
  print(index, value)
  # 0 (1, 10)
  # 1 (2, 20)
  # 2 (3, 30)
  # 3 (4, 40)
  # 4 (5, 50)
  # 5 (6, 60)

for index, value in enumerate(dict_num.items(), 1):
  print(index, value)
  # 1 (1, 10)
  # 2 (2, 20)
  # 3 (3, 30)
  # 4 (4, 40)
  # 5 (5, 50)
  # 6 (6, 60)

for index, (key, value) in enumerate(dict_num.items(), 1):
  print(key, value)
  # 1 10
  # 2 20
  # 3 30
  # 4 40
  # 5 50
  # 6 60

for index, (key, value) in enumerate(dict_num.items(), 1):
  print(index, (key, value))
  # 1 (1, 10)
  # 2 (2, 20)
  # 3 (3, 30)
  # 4 (4, 40)
  # 5 (5, 50)
  # 6 (6, 60) 

for index, (key, value) in enumerate(dict_num.items(), 1):
  print(index, key, value)
  # 1 1 10
  # 2 2 20
  # 3 3 30
  # 4 4 40
  # 5 5 50
  # 6 6 60 

#///////////////////////////////////////////////////////////////////////////////////////////

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

count = 1

for n in dict_num:
  print(count, n, dict_num[n])
  count += 1
  
  # 1 1 10
  # 2 2 20
  # 3 3 30
  # 4 4 40
  # 5 5 50
  # 6 6 60

#///////////////////////////////////////////////////////////////////////////////////////////

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

c = 1

for k, v in dict_num.items():
  print(c, k, v)
  c += 1
  
  # 1 1 10
  # 2 2 20
  # 3 3 30
  # 4 4 40
  # 5 5 50
  # 6 6 60