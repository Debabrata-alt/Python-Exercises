#  Write a Python program to calculate the sum of harmonic series upto n terms.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# 1 + 1/2 + 1/3 + 1/4 + 1/5 +.............

def harmonic_sum(n):
  if n < 2:
    return 1
  else: 
    return 1/n + harmonic_sum(n - 1)


print(harmonic_sum(4)) # 2.083333333333333
print(harmonic_sum(5)) # 2.283333333333333
print(harmonic_sum(7)) # 2.5928571428571425

