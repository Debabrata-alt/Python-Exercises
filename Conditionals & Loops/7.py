# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

def myFunc(row, column):
  myList = []
  temp_list = []
  for i in range(row):
    for j in range(column):
      temp_list += [i * j]
    myList.append(temp_list)
    temp_list = []
  return myList

print(myFunc(3, 4))
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]