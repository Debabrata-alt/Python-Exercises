# Write a Python program to remove key-value pairs from a list of dictionaries.

my_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}] 

for el in my_list:
  del el["key1"]

print(my_list) # [{'key2': 'value2'}, {'key2': 'value4'}]

#//////////////////////////////////////////
# 2nd way - using pop() method

my_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}] 

for el in my_list:
  el.pop("key1")

print(my_list) # [{'key2': 'value2'}, {'key2': 'value4'}]
