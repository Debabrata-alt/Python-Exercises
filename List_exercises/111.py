# Sum a list of numbers. Write a Python program to sum the first number with the second and divide it by 2, then sum the second with the third and divide by 2, and so on.
# Original list:
# [1, 2, 3, 4, 5, 6, 7]
# Sum the said list of numbers:
# [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
# Original list:
# [0, 1, -3, 3, 7, -5, 6, 7, 11]
# Sum the said list of numbers:
# [0.5, -1.0, 0.0, 5.0, 1.0, 0.5, 6.5, 9.0]

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [0, 1, -3, 3, 7, -5, 6, 7, 11]

def func(inp_list):
  return list((inp_list[n] + inp_list[n + 1])/2 for n in range(0, len(inp_list) - 1))


print(func(list1))
# [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]

print(func(list2))
# [0.5, -1.0, 0.0, 5.0, 1.0, 0.5, 6.5, 9.0]