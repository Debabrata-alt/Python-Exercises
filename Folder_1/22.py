# List all prime numbers 1-1000

num_list = []

for num in range(2, 1001):
  for n in range(2, num):
    if num % n == 0:
      break
  else: 
    num_list.append(num)

print(f"All prime numbers 1 to 1000:\n{num_list}")