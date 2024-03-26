# Write a Python program to assess if a file is closed or not.

f = open("demo.txt", mode="r")

print(f.closed) # False

f.close()

print(f.closed) # True