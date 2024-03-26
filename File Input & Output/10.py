# Write a Python program to get the file size of a plain file.

import os

def file_size():
  fname = "demo.txt"
  statInfo = os.stat(fname)
  return statInfo.st_size

print("File size in bytes of a plain file: ", file_size())
# File size in bytes of a plain file: 1557