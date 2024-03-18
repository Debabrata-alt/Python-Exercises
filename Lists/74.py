# Write a Python program to join two given list of lists of the same length, element wise.
# Original lists:
# [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
# Original lists:
# [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# Join the said two lists element wise:
# [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]

num_list1 = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
num_list2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]

char_list1 = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
char_list2 = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]


def func(input_list1, input_list2):
  return [el[0] + el[1] for el in zip(input_list1, input_list2)]


print(func(num_list1, num_list2))
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]

print(func(char_list1, char_list2))
# [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]