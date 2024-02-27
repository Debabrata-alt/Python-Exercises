# List all harshad numbers 1-1000
# 153 / (1 + 5 + 3) = 17
# 153 % (1 + 5 + 3) == 0

divisible_in_max_10s = 0
no_of_digits = 0
num_list = []
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
  for i in range(no_of_digits):
    digit_i = int(num_temp / divisible_in_max_10s)
    sum += digit_i
    remainder = num_temp % divisible_in_max_10s
    num_temp = remainder
    divisible_in_max_10s /= 10
  if num % sum == 0:
    num_list.append(num)
  sum = 0

print(f"All Harshad numbers 1 to 1000:\n{num_list}")