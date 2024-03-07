# Write a Python program to sort each sublist of strings in a given list of lists.
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]


def sort_sublists(input_list):
  # Use the 'map' function to sort each sublist in 'input_list' and convert the result to a list
  result = list(map(sorted, input_list))
  return result

color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
num1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

print(sort_sublists(color1))
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

print(sort_sublists(num1))
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
