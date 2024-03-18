# print stars in this pattern:
#         *
#        **
#       ***
#      ****
#     *****

rows = int(input("Enter the no of rows: "))

for n in range(1, rows + 1):
  print(" " * (rows - n) + "*" * n)


# 1 - 4
# 2 - 3
# 3 - 2
# 4 - 1
# 5 - 0