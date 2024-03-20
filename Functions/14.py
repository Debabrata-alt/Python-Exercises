# Write a Python program that invokes a function after a specified period of time.

# Import specific functions 'sleep' from the 'time' module and the 'math' module
from time import sleep
import math

# Define a function named 'delay' that delays the execution of a function by the given milliseconds
def delay(fn, ms, arg):
  # Sleep for the specified number of seconds (milliseconds/1000 = seconds)
  sleep(ms / 1000)
  
  return fn(arg)


# Print the square root of 16 after a delay of 100 milliseconds
print(delay(lambda x: math.sqrt(x), 100, 16)) # 4.0

# Print the square root of 100 after a delay of 1000 milliseconds
print(delay(lambda x: math.sqrt(x), 1000, 100)) # 10.0

# Print the square root of 25100 after a delay of 2000 milliseconds
print(delay(lambda x: math.sqrt(x), 2000, 25100)) # 158.42979517754858
