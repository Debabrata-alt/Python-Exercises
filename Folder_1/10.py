# Check if a number is disarium number or not.
# 1^1 + 7^2 + 5^3 = 1 + 49 + 125 = 175

num = int(input("Enter the number: "))
divisible_in_max_10s = 0
no_of_digits = 0
sum = 0

if num < 10:
  divisible_in_max_10s = 1
  no_of_digits = 1
else:  
  for n in range(1, num):
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
  print(f"{num} is a disarium number")
else:
  print(f"{num} is not a disarium number")



# 175 / 100 = 1
# 175 % 100 = 75

# 75 / 10 = 7
# 75 % 10 = 5

# 5 / 1 = 5
# 5 % 1 = 0