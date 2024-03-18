# Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.
# Sample Data:
# ("1981-1991") -> 2
# ("2000-2020") -> 6


def func(range_years):
  
  start_year, end_year = map(int, range_years.split('-'))
    
  # Use a generator expression to count the leap years within the specified range
  return sum(is_leap_year(year) for year in range(start_year, end_year + 1))


# Define a function to check if a given year is a leap year
def is_leap_year(y):
  # Check the leap year conditions and return True if it's a leap year, otherwise False
  if y % 400 == 0:
    return True
  if y % 100 == 0:
    return False
  if y % 4 == 0:
    return True
  else:
    return False


print(func("1981-1991")) # 2

print(func("2000-2020")) # 6


#////////////////////////////////////////////////////

# NOTE: 
# True == 1
# False == 0