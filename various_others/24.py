# Check if a number is Ugly number or not.
# An ugly number is a positive number whose prime factors only include 2, 3, or 5. This means that an ugly number can be divided by 2, 3, or 5, but not by any other prime number.

num = int(input("Enter the number: "))

prime_factors_list = []
prime_factor = 0

for n in range(2, num + 1):
  # check if n is prime number
  for i in range(2, n):
    if n % i == 0:
      break
  else: 
    if num % n == 0:
      prime_factors_list.append(n)

print(f"List of all prime factors:\n{prime_factors_list}")
# print(list2)

for factor in prime_factors_list:
  if factor != 2 and factor != 3 and factor != 5:
    prime_factor = factor

if prime_factor not in prime_factors_list:
  print(f"{num} is an ugly number")
else:
  print(f"{num} is not an ugly number")

