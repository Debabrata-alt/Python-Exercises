# Write a general-purpose function to convert any given year into its roman equivalent. The following table shows the roman equivalents of decimal numbers:
# Decimal   Roman   Decimal  Roman
# 1           i      100      c
# 5           v      500      d
# 10          x     1000      m
# 50          l

# Example:
# Roman equivalent of 1988 is mdcccclxxxviii
# Roman equivalent of 1525 is mdxxv

year = int(input("Enter the year: "))

def year_to_roman(year):
  year_to_roman = ""
  # 1(1000)
  quotient = int(year / 1000)
  remainder = year % 1000
  year_to_roman += quotient * "m"
  # 2(500)
  quotient = int(remainder / 500)
  remainder %= 500
  year_to_roman += quotient * "d"
  # 3(100)
  quotient = int(remainder / 100)
  remainder %= 100
  year_to_roman += quotient * "c"
  # 4(50)
  quotient = int(remainder / 50)
  remainder %= 50
  year_to_roman += quotient * "l"
  # 5(10)
  quotient = int(remainder / 10)
  remainder %= 10
  year_to_roman += quotient * "x"
  # 6(5)
  quotient = int(remainder / 5)
  remainder %= 5
  year_to_roman += quotient * "v"
  # 7(1)
  quotient = int(remainder / 1)
  remainder %= 1
  year_to_roman += quotient * "i"
  print(f"Year to Roman: {year_to_roman}")


year_to_roman(year)
