# Write a Python program to extract year, month, date and time using Lambda.
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# Import the 'datetime' module to work with date and time
import datetime

# Get the current date and time 
now = datetime.datetime.now()

print(now)
# 2024-03-20 17:02:46.829722

year = lambda el: el.year
month = lambda el: el.month
day = lambda el: el.day
hour = lambda el: el.hour
minute = lambda el: el.minute
second = lambda el: el.second
time = lambda el: el.time()

print(year(now)) # 2024
print(month(now)) # 3
print(day(now)) # 20
print(hour(now)) # 17
print(minute(now)) # 2
print(second(now)) # 46
print(time(now)) # 17:02:46.829722