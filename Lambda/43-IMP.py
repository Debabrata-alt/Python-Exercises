# Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
# Original Tuple:
# ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (30.5, 34.25, 27.0)
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (25.5, -18.0, 3.75)

tuplex1 = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
tuplex2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

def func(mytuple):
  return tuple(map(lambda el: sum(el)/len(el), zip(*mytuple)))

print(func(tuplex1))
# (30.5, 34.25, 27.0)

print(func(tuplex2))
# (25.5, -18.0, 3.75)

#///////////////////////////////////////////////////////////////////////////////////////

tuplex1 = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
tuplex2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

def func(mytuple):
  return tuple(sum(el)/len(el) for el in zip(*mytuple))

print(func(tuplex1))
# (30.5, 34.25, 27.0)

print(func(tuplex2))
# (25.5, -18.0, 3.75)



