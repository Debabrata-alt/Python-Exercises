# List out all amstrong numbers 1-1000

num_list = []
divisible_in_max_10s = 0
no_of_digits = 0
sum = 0 

for num in range(1, 1001):
  for n in range(num):
    if int(num / 10 ** n) < 10:
      divisible_in_max_10s = 10 ** n
      no_of_digits = n + 1
      break
  num_temp = num
  while divisible_in_max_10s > 0:
    num_added = int(num_temp / divisible_in_max_10s) 
    sum += (num_added ** no_of_digits) 
    num_remainder = num_temp % divisible_in_max_10s
    num_temp = num_remainder
    divisible_in_max_10s = divisible_in_max_10s / 10
  if sum == num:
    num_list.append(num)
  sum = 0

print(f"Here is the list of all armstrong numbers from 1 to 1000:\n{num_list}")