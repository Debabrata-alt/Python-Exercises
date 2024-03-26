# Please write an examples of writelines() method.

# The writelines() method writes the items of a list to the file. Where the texts will be inserted depends on the file mode and stream position. 
# mode="a" : The texts will be inserted at the current file stream position, default at the end of the file.

# The writelines() method in Python is used to write a sequence of strings to a file. It takes an iterable object as an argument, which is typically a list of strings. The method writes each string in the iterable to the file, one after the other. The writelines() method does not add a newline character (\n) to the end of each string, so you need to add it yourself if you want each string to appear on a new line in the file.

# Creating a new file
with open("demo7.txt", mode="w") as f:
  f.writelines(["This is the first line.\n", "My name is Raju.\n", "I am 40 years old.\n", "I am a very good person.\n", "I learning programming.\n", "programming is fun!\n"])

# appending lines at the end of the file
with open("demo7.txt", mode="a") as f:
  f.writelines(["I am appending a few more lines.\n", "I want to create good software.\n", "This is the current last line.\n"])

