# print stars in this pattern:
# *
# ***
# *****
# *******

rows = int(input("Enter the no of rows: "))

for row in range(1, rows + 1):
  print("*" * ((row * 2) - 1))