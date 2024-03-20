nums = [10, 20, 30, (10, 20), 40]
temp_list = []

for el in nums:
  if type(el) == tuple:
    break
  temp_list.append(el)

print(len(temp_list)) # 3

#////////////////////////////////////////////////////////////////////////////////

nums = [10, 20, 30, (10, 20), 40]
temp_list = []

for el in nums:
  if type(el) is tuple:
    break
  temp_list.append(el)

print(len(temp_list)) # 3

#////////////////////////////////////////////////////////////////////////////////

nums = [10, 20, 30, (10, 20), 40]
temp_list = []

for el in nums:
  if isinstance(el, tuple):
    break
  temp_list.append(el)

print(len(temp_list)) # 3

