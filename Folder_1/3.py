# print stars in this pattern:
# *******
# *****
# ***
# *

rows = int(input("Enter the no of rows: "))

for row in range(1, rows + 1):
  print("*" * ((rows * 2) - (2 * row - 1)))


# 4* 2 - 1
# 4* 2 - 3
# 4 * 2 - 5
# 4* 2 - 7