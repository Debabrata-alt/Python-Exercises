# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple:
# ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# Average value of the numbers of the said tuple of tuples:
# [30.5, 34.25, 27.0, 23.25]
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# [25.5, -18.0, 3.75]

tuplex1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
tuplex2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))


def func(inp_tup):
  return [sum(el)/len(el) for el in zip(*inp_tup)]


print(func(tuplex1)) # [30.5, 34.25, 27.0, 23.25]
print(func(tuplex2)) # [25.5, -18.0, 3.75]