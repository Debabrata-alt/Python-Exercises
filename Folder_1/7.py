# write a program to check if a number is an amstrong number or not.

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

while divisible_in_max_10s > 0:
  num_added = int(num_temp / divisible_in_max_10s) 
  sum += (num_added ** no_of_digits) 
  num_remainder = num_temp % divisible_in_max_10s
  num_temp = num_remainder
  divisible_in_max_10s = divisible_in_max_10s / 10

if sum == num:
  print(f"{num} is an amstrong number")
else:
  print(f"{num} is not an amstrong number")



