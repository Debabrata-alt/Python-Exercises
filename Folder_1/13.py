# write down the multiplication table of a given number for a given times and find the sum of all multiplied nos.

multiplicand = int(input("Enter the multiplicand: "))
no_of_multipliers = int(input("Enter the no of multipliers: "))
sum = 0
for m in range(0, no_of_multipliers + 1):
  multiplied_no = multiplicand * m
  # print(f"{multiplicand} * {m} = {multiplicand * m}")
  print(f"{multiplicand} * {m} = {multiplied_no}")
  sum += multiplied_no

print(f"sum of all multiplied nos = {sum}")
