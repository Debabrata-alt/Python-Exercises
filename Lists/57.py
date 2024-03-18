# Write a Python program to calculate the product of the unique numbers in a given list.
# Original List : [10, 20, 30, 40, 20, 50, 60, 40]
# Product of the unique numbers of the said list: 720000000

org_list = [10, 20, 30, 40, 20, 50, 60, 40]

# Remove duplicates by converting the list to set
list_unique_nums = list(set(org_list))

product = 1

for el in list_unique_nums:
  product *= el


print(product) # 720000000