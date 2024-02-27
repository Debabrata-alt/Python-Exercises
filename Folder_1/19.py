# Check if a number is Harshad number or not.
# 153 / (1 + 5 + 3) = 17
# 153 % (1 + 5 + 3) == 0

num = int(input("Enter the number: "))
divisible_in_max_10s = 0
no_of_digits = 0
sum = 0

for n in range(1, num):
  if int(num / 10 ** n) < 10:
    divisible_in_max_10s = 10 ** n
    no_of_digits = n + 1
    break

num_temp = num

for n in range(no_of_digits):
  digit_n = int(num_temp / divisible_in_max_10s)
  sum += digit_n
  remainder = num_temp % divisible_in_max_10s
  num_temp = remainder
  divisible_in_max_10s /= 10

if num % sum == 0:
  print(f"{num} is a Harshad number")
else:
  print(f"{num} is not a Harshad number")
