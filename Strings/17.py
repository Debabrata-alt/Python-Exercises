# Exponentiation calculation
# Calculate the value: n1 to the power n2

num = input("Enter the nos: ").split(", ")
n1, n2 = int(num[0]), int(num[1])  # 5, 3

def power(n1, n2):
  n3 = 1
  while n2 >= 1: 
    n4 = n1 * n3
    n3 = n4
    n2 -= 1
  return n4

pow = power(n1, n2)  # 125

print(f"{n1} to the power {n2} = {pow}")


#///////////////////////////////////////////////////////////////////////
"""
(FOR REFERENCE)
-------------------------------------------------------------------------

n1_list = str(n1).split(".")
n2_list = str(n2).split(".")
pow_list = str(pow).split(".")

if (len(n1_list[1]) == 1 and str(n1).endswith("0")) and (len(n2_list[1]) == 1 and str(n2).endswith("0")) and (len(pow_list[1]) == 1 and str(pow).endswith("0")):
  print(f"{int(n1)} to the power {int(n2)} = {int(pow)}")
elif (len(n1_list[1]) == 1 and str(n1).endswith("0")):
  print(f"{int(n1)} to the power {n2} = {round(pow, 3)}")
elif (len(n2_list[1]) == 1 and str(n2).endswith("0")):
  print(f"{n1} to the power {int(n2)} = {round(pow, 3)}")
elif (len(pow_list[1]) == 1 and str(pow).endswith("0")):
  print(f"{n1} to the power {n2}: {int(pow)}")
else:
  print(f"{n1} to the power {n2} = {round(pow, 3)}")

"""