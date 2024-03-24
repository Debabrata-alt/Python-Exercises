# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz

for n in range(1, 51):
  if n % 3 == 0:
    print("Fizz")
    continue
  elif n % 5 == 0:
    print("Buzz")
    continue
  elif n % 3 == 0 and n % 5 == 0:
    print("Fizzbuzz")
    continue
  print(n)

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# Fizz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# Fizz
# 31
# 32
# Fizz
# 34
# Buzz
# Fizz
# 37
# 38
# Fizz
# Buzz
# 41
# Fizz
# 43
# 44
# Fizz
# 46
# 47
# Fizz
# 49
# Buzz