# Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output:
# True
# False

myStr1 = "avanti is good"
myStr2 = "pinku is good"

fn = lambda myStr: myStr.startswith("a")

print(fn(myStr1)) # True
print(fn(myStr2)) # False

#////////////////////////////////////////////////////////////////////

fn = lambda myStr: True if myStr.startswith('a') else False

print(fn(myStr1)) # True
print(fn(myStr2)) # False

