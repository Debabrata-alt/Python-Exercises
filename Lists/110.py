# Write a Python program to check if the first digit or character of each element in a list is the same.
# Original list:
# [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# True
# Original list:
# [1234, 922, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# False
# Original list:
# ['aabc', 'abc', 'ab', 'a']
# Check if first character in each element of the said given list is same or not!
# True
# Original list:
# ['aabc', 'abc', 'ab', 'ha']
# Check if first character in each element of the said given list is same or not!
# False

list1 = [1234, 122, 1984, 19372, 100]
list2 = [1234, 922, 1984, 19372, 100]

list3 = ['aabc', 'abc', 'ab', 'a']
list4 = ['aabc', 'abc', 'ab', 'ha']

def func(inp_list):
  return all(str(el)[0] == str(inp_list[0])[0] for el in inp_list)

print(func(list1)) # True
print(func(list2)) # False
print(func(list3)) # True
print(func(list4)) # False