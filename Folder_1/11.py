# List out all disarium numbers 1-1000
# 1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175

num_list = []
divisible_in_max_10s = 0
no_of_digits = 0
sum = 0 

for num in range(1, 10):
  num_list.append(num)

for num in range(10, 1001):
  for n in range(num):
    if int(num / 10 ** n) < 10:
      divisible_in_max_10s = 10 ** n
      no_of_digits = n + 1
      break
  num_temp = num
  for i in range(1, no_of_digits + 1):
    num_added = int(num_temp / divisible_in_max_10s)
    sum += (num_added ** i)
    num_remainder = num_temp % divisible_in_max_10s
    num_temp = num_remainder
    divisible_in_max_10s = divisible_in_max_10s / 10
  if sum == num:
    num_list.append(num)
  sum = 0

# print(num_list)
all_disarium_nos = " ".join(str(num) for num in num_list)
print(f"All disarium numbers from 1 to 1000:\n{all_disarium_nos}")