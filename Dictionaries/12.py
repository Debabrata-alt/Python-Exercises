# Write a Python program to get the maximum and minimum values of a dictionary.

my_dict = {'x': 500, 'y': 5874, 'z': 560}

x = max(value for value in my_dict.values())

print(x) # 5874

y = min(value for value in my_dict.values())

print(y) # 500

#/////////////////////////////////////////////////////////////

my_dict = {'x': 500, 'y': 5874, 'z': 560} 

max_key = max(my_dict, key=lambda a: my_dict[a])

print(max_key) # y

max_val = my_dict[max_key] 

print(max_val) # 5874

min_key = min(my_dict, key=lambda a: my_dict[a])

print(min_key) # x

min_val = my_dict[min_key]

print(min_val) # 500

#/////////////////////////////////////////////////////////

my_dict = {'x': 500, 'y': 5874, 'z': 560} 

max_key = max(my_dict.keys(), key=lambda a: my_dict[a])

min_key = min(my_dict.keys(), key=lambda a: my_dict[a])

print(max_key) # y

print(min_key) # x

max_val = my_dict[max_key] 

min_val = my_dict[min_key] 

print(max_val) # 5874
print(min_val) # 500

