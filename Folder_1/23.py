# Check if a positive number has only 3 prime factors - 2, 3 and 5. 
# This means that this number can be divided only by 2, 3 and 5, but not by any other prime number.
# NOTE: This is not an ugly number check.

num = int(input("Enter the number: "))

list1 = [2, 3, 5]
list2 = []
other_prime_factors_list = []
other_prime_factors_str = ""

for n in range(2, num + 1):
  # check if n is prime number
  for i in range(2, n):
    if n % i == 0:
      break
  else: 
    if num % n == 0:
      if n in list1:
        list2.append(n)
      else:
        other_prime_factors_list.append(n)
        list1.append(n)
        other_prime_factors_str = ", ".join(str(num) for num in other_prime_factors_list)

print(f"List of all prime factors:\n{list1}")
# print(list2)

if list1 == list2:
  print(f"Great! primary factors of {num} are only 2, 3 and 5. So it fulfils our condition.")
else:
  print(f"Sorry, {num} does not fulfil our condition. We need only 2, 3 and 5 as primary factors. But {num} has other primary factors too, which {"is" if len(other_prime_factors_list) == 1 else "are"} {other_prime_factors_str}")

