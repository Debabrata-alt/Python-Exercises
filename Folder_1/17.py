# List all palindrome numbers 1-10000

divisible_in_max_10s = 0
no_of_digits = 0
num_list = []
reversed_num_str = ""

for num in range(1, 10):
  num_list.append(num)

for num in range(10, 10001):
  for n in range(num):
    if int(num / 10 ** n) < 10:
      divisible_in_max_10s = 10 ** n
      no_of_digits = n + 1
      break
  num_temp = num
  for i in range(no_of_digits):
    digit_i = int(num_temp / divisible_in_max_10s)
    reversed_num_str = f"{digit_i}{reversed_num_str}"
    remainder = num_temp % divisible_in_max_10s
    num_temp = remainder
    divisible_in_max_10s /= 10
  reversed_num = int(reversed_num_str)
  if num == reversed_num:
    num_list.append(num)
  reversed_num_str = ""

all_palindrome_nos = " ".join(str(num) for num in num_list)

print(f"All palindrome numbers 1 to 10000:\n{all_palindrome_nos}")