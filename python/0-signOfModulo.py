# For n % k sign is same as sign of k
# In case of k > 0, look for closest lesser multiple and subtract from it
# In case of k < 0, look for just greater multiple and subtract from it
print(41 % 7) # k > 0, closest lesser multiple = 35, output = 41 - 35 = 6
print(-41 % 7) # k > 0, closest lesser multiple = -42, output = 41 - (-42) = 1
print(41 % -7) # k < 0, closest greater multiple = 42, output = 41 - 42 = -1
print(-41 % -7) # k < 0, closest lesser multiple = -35, output = -41 - (-35) = -6