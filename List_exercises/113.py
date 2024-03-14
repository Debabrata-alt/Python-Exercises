# Write a Python program to calculate the sum of two lowest negative numbers in a given array of integers.
# An integer (from the Latin integer meaning "whole") is colloquially defined as a number that can be written without a fractional component. For example, 21, 4, 0, and -2048 are integers.
# Original list elements: [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
# Sum of two lowest negative numbers of the said array of integers: -27
# Original list elements: [-4, 5, -2, 0, 3, -1, 4, 9]
# Sum of two lowest negative numbers of the said array of integers: -6

list1 = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
list2 = [-4, 5, -2, 0, 3, -1, 4, 9]

def func(inp_list):
  return sum(sorted(inp_list)[:2])

print(func(list1)) # -27
print(func(list2)) # -6