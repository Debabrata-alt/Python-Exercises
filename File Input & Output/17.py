# Write a Python program that takes a text file as input and returns the number of words of a given text file.
# Note: Some words can be separated by a comma with no space.

with open("demo.txt", mode="r") as f:
  data = f.read()
  # Replace the characters (,.: and -) with whitespaces in the 'data' string
  # NOTE: 4 types of characters, each one is replaced with a whitespace
  data = data.translate(data.maketrans(",.:-", "    "))

print(data)

dataList = data.split()

print(f"Number of words in the file: {len(dataList)}")
# Number of words in the file: 233