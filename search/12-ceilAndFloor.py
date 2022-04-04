import random

def floorUtil(a, l, r, x):
    if l > r:
        return None
    m = l + (r - l) // 2
    if a[m] == x:
        return a[m]
    if a[m] < x and (m == r or a[m + 1] > x):
        return a[m]
    if a[m] < x:
        return floorUtil(a, m + 1, r, x)
    return floorUtil(a, l, m - 1, x)
    

def floor(a, x):
    n = len(a)
    return floorUtil(a, 0, n - 1, x)

def ceil(a, x):
    n = len(a)
    return ceilUtil(a, 0, n - 1, x)

def ceilUtil(a, l, r, x):
    if l > r:
        return None
    m = l + (r - l) // 2
    if a[m] == x:
        return a[m]
    if a[m] > x and (l == m or a[m-1] < x):
        return a[m]
    if a[m] > x:
        return ceilUtil(a, l, m - 1, x)
    return ceilUtil(a, m + 1, r, x)

a = [1, 2, 8, 10, 10, 12, 19]

for i in range(20):
    x = random.randint(0, 25)
    print("Ceil of " + str(x) + " is: "+ str(ceil(a, x)))
    print("Floor of " + str(x) + " is: "+ str(floor(a, x)))