# Write a Python program to wrap a given string into a paragraph with a given width.

import textwrap 

def txt_format(text, width):
  return textwrap.fill(text.strip(), width)

# Wrap input string to width w
print(textwrap.fill("The quick brown fox.", 10)) 
# The quick
# brown fox.