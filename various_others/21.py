# Check if a number is prime number or not.

num = int(input("Enter the number: "))

for n in range(2, num):
  if num % n == 0:
    print(f"{num} is not a prime number")
    break
else:
  print(f"{num} is a prime number")
  