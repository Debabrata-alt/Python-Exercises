# Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.
# Original list:
# [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# Index positions of the maximum value of the said list:
# 7
# Index positions of the minimum value of the said list:
# 3, 11

org_list = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]

max_val = max(org_list)
min_val = min(org_list)

print(max_val) # 667
print(min_val) # 10

max_val_indices_list = [i for i, e in enumerate(org_list) if e == max_val]

min_val_indices_list = [i for i, e in enumerate(org_list) if e == min_val]

print(max_val_indices_list) # [7]
print(min_val_indices_list) # [3, 11]

#//////////////////////////////////////////////////////////////////////////////////////////

org_list = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]

max_val = max(org_list)
min_val = min(org_list)

max_val_indices_list =[]
min_val_indices_list = []

for i, e in enumerate(org_list):
  if e == max_val:
    max_val_indices_list.append(i)
  if e == min_val:
    min_val_indices_list.append(i)

print(max_val) # 667
print(min_val) # 10

print(max_val_indices_list) # [7]
print(min_val_indices_list) # [3, 11]