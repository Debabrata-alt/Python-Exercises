# List out all deficient numbers 1-1000

num_list = []
sum = 0

for num in range(1, 1001):
  for n in range(1, num + 1):
    if num % n == 0:
      sum += n
  if sum < 2 * num:
    num_list.append(num)
  sum = 0

# print(num_list)
all_deficient_nos = " ".join(str(num) for num in num_list)
print(f"All deficient numbers from 1 to 1000:\n{all_deficient_nos}")