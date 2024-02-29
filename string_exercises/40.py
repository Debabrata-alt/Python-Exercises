# Write a Python program to split a string on the last occurrence of the delimiter.
# [Use rsplit() method]

string = "w,3,r,e,s,o,u,r,c,e"

print(string.rsplit(",", 1))  # ['w,3,r,e,s,o,u,r,c', 'e']
print(string.rsplit(",", 2))  # ['w,3,r,e,s,o,u,r', 'c', 'e']
print(string.rsplit(",", 3))  # ['w,3,r,e,s,o,u', 'r', 'c', 'e']
print(string.rsplit(",", 4))  # ['w,3,r,e,s,o', 'u', 'r', 'c', 'e']