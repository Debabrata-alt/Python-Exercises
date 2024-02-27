# Check if a number is deficient number or not.

num = int(input("Enter the number: "))

sum = 0
for n in range(1, num + 1):
  if num % n == 0:
    sum += n

if sum < 2 * num:
  print(f"{num} is a deficient number")
else:
  print(f"{num} is not a deficient number")