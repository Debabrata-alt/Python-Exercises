# Write a Python program to check if a given string contains an element that is present in a list.
# The original string and list:
# https://www.w3resource.com/python-exercises/list/
# ['.com', '.edu', '.tv']
# Check if https://www.w3resource.com/python-exercises/list/ contains an element, which is present in the list ['.com', '.edu', '.tv']
# True
# The original string and list: https://www.w3resource.net
# https://www.w3resource.net
# ['.com', '.edu', '.tv']
# Check if https://www.w3resource.net contains an element, which is present in the list ['.com', '.edu', '.tv']
# False

string1 = "https://www.w3resource.com/python-exercises/list/"
list1 =  ['.com', '.edu', '.tv']

string2 =  "https://www.w3resource.net"
list2 = ['.com', '.edu', '.tv']

def func(string, inp_list):
  return any(el for el in inp_list if el in string)


print(func(string1, list1)) # True

print(func(string2, list2)) # False