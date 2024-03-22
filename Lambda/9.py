# Check if the given strings are numeric by using the 'is_num' lambda function and print the results.

# Remove the first decimal point in the string, then check if it is numeric or not.
is_num = lambda num: num.replace(".", "", 1).isdigit()


print(is_num('26587')) # True
print(is_num('4.2365')) # True
print(is_num('-12547')) # False
print(is_num('00')) # True
print(is_num('A001')) # False
print(is_num('001')) # True

#///////////////////////////////////////////

# Exclude the minus sign ('-') from the beginning of the string if it is present in the beginning.
is_num1 = lambda n: is_num(n[1:]) if n[0] == "-" else is_num(n)

print(is_num1('-16.4')) # True
print(is_num1('-24587.11')) # True