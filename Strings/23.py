# Write a Python program to display formatted text (width=50) as output.


# Import the 'textwrap' module, which provides text formatting capabilities.
import textwrap

# Define a multi-line string 'sample_text' with a text content.
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted, dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''

# Print an empty line for spacing.
print()

# Use the 'textwrap.fill' function to format the 'sample_text' with a line width of 50 characters.
# This function wraps the text to fit within the specified width and prints the result.
print(textwrap.fill(sample_text, width=50))

# Print an empty line for spacing.
print()
