#  Write a Python program to compute the element-wise sum of given tuples.
# Original lists:
# (1, 2, 3, 4)
# (3, 5, 2, 1)
# (2, 2, 3, 1)
# Element-wise sum of the said tuples:
# (6, 9, 8, 6)

tuplex1 = 1, 2, 3, 4
tuplex2 = 3, 5, 2, 1
tuplex3 = 2, 2, 3, 1

def func(tuplex1, tuplex2, tuplex3):
  return tuple(sum(el) for el in zip(tuplex1, tuplex2, tuplex3))


print(func(tuplex1, tuplex2, tuplex3))
# (6, 9, 8, 6)
