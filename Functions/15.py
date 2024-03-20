# Write a Python program that invokes a function after a specified period of time.

from time import sleep
import math

def delay(fn, ms, *args):
  for arg in args:
    # delay code execution for the specified number of seconds (milliseconds/1000 = seconds)
    sleep(ms/1000)
    print(fn(arg))


delay(lambda x: math.sqrt(x), 2000, 324, 400, 484, 576)
# 18.0
# 20.0
# 22.0
# 24.0