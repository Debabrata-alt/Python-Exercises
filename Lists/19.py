# Write a Python program to sort a list of nested dictionaries.


my_list = [{"key": {"subkey": 1}}, {"key": {"subkey": 10}}, {"key": {"subkey": 5}}]

# sort in ascending order
my_list.sort(key = lambda el: el["key"]["subkey"])

print(my_list)
# [{'key': {'subkey': 1}}, {'key': {'subkey': 5}}, {'key': {'subkey': 10}}]

#///////////////////////////////////////

# sort in descending order

my_list.sort(key = lambda el: el["key"]["subkey"], reverse = True)

print(my_list)
# [{'key': {'subkey': 10}}, {'key': {'subkey': 5}}, {'key': {'subkey': 1}}]