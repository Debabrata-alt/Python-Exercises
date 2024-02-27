# check if the number is palindrome number or not.

num = int(input("Enter the number: "))

divisible_in_max_10s = 0
no_of_digits = 0
reversed_num_list = []
reversed_num_str = ""

for n in range(1, num):
  if int(num / 10 ** n) < 10:
    divisible_in_max_10s = 10 ** n
    no_of_digits = n + 1
    break

num_temp = num

for n in range(no_of_digits):
  digit_n = int(num_temp / divisible_in_max_10s)
  reversed_num_list = [digit_n] + reversed_num_list
  # reversed_num_str = str(digit_n) + reversed_num_str
  reversed_num_str = f"{digit_n}{reversed_num_str}"
  remainder = num_temp % divisible_in_max_10s
  num_temp = remainder
  divisible_in_max_10s /= 10

reversed_num = int(reversed_num_str)

if num == reversed_num:
  print(f"{num} is a palindrome number")
else:
  print(f"{num} is not a palindrome number")
