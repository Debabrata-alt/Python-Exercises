# Check if a number is abundant number or not.

num = int(input("Enter the number: "))

sum = 0
for n in range(1, num):
  if num % n == 0:
    sum += n
if sum > num:
  print(f"{num} is an abundant number")
  abundance = sum - num
  print(f"abundance = {abundance}")
else:
  print(f"{num} is not an abundant number")