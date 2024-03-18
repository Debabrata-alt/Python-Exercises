# Write a Python program to find the specified number of largest products from two given lists, multiplying an element from each list.
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [3, 6, 8, 9, 10, 6]
# 3 Number of largest products from the said two lists:
# [60, 54, 50]
# 4 Number of largest products from the said two lists:
# [60, 54, 50, 48]

main_list = [3, 6, 8, 9, 10, 6]
mul_list = [1, 2, 3, 4, 5, 6]

def calculate(main_list, mul_list, num):
  total_list = [e * el for el in main_list for e in mul_list]
  # [3, 6, 9, 12, 15, 18, 6, 12, 18, 24, 30, 36, 8, 16, 24, 32, 40, 48, 9, 18, 27, 36, 45, 54, 10, 20, 30, 40, 50, 60, 6, 12, 18, 24, 30, 36]
  sorted_list = sorted(total_list, reverse=True)
  return sorted_list[:num]


print(calculate(main_list, mul_list, 3))
# [60, 54, 50]

print(calculate(main_list, mul_list, 4))
# [60, 54, 50, 48]