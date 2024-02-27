# print stars in this pattern:
# *****
# ****
# ***
# **
# *

rows = int(input("Enter the no of rows: "))

for row in range(rows):
  print("*" * (rows - row))
