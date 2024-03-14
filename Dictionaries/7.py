# Write a Python program to sum all the items in a dictionary.

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}

result = sum(value for value in my_dict.values()) 

print(result) # 293