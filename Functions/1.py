# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def func(myStr):
  newStr = ""
  for n in range(len(myStr)):
    newStr += myStr[-(n + 1)]
  return newStr

print(func("1234abcd")) # dcba4321

#/////////////////////////////////////////////

l = "".join(reversed("1234abcd"))

print(l) # dcba4321

#/////////////////////////////////////////////

x = "1234abcd"[::-1]

print(x) # dcba4321