# Write a Python program to copy the contents of a file to another file.

from shutil import copyfile

# Copying the content of 'demo.txt' file to 'demo2.txt' file (Note that the 'demo2.txt' file will be created automatically with all the content of 'demo.txt' filein it)

copyfile("demo.txt", "demo2.txt")