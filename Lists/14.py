# Write a Python program to access the index of a list.


def func(list):
  for index, element in enumerate(list):
    print("Element: {}, Index: {}".format(element, index))


func([5, 15, 35, 8, 98])

# Element: 5, Index: 0
# Element: 15, Index: 1
# Element: 35, Index: 2
# Element: 8, Index: 3
# Element: 98, Index: 4

