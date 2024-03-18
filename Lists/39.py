# Write a Python program to sort a given matrix in ascending order according to the sum of its rows.
# Original Matrix:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

mat1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
mat2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

mat1.sort(key=sum)

mat2.sort(key=sum)

print(mat1)
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]

print(mat2)
# [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]