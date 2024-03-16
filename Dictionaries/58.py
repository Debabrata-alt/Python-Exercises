# Write a Python program to check if a specific key and a value exist in a dictionary.
# Original dictionary:
# [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]
# Check if a specific Key and a value exist in the said dictionary:
# True
# True
# True
# False
# False
# False

myList = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]


def func(myList, key, value):
  return any(key == k and value == v for el in myList for k, v in el.items())


print(func(myList, 'student_id', 1)) # True

print(func(myList, 'name', 'Brian Howell')) # True

print(func(myList, 'class', 'VII')) # True

print(func(myList, 'class', 'I')) # False

print(func(myList, 'name', 'Brian Howelll')) # False

print(func(myList, 'student_id', 11)) # False