# 16 17 18 19 20
# 21 22 24 25 26 27 28 29 30
# 31 32 33 34 35 36 37 38 39 40
# 41 42 43 44 45 46 47 48 49
# 51 52
import random

def search(a, x, k):
    if k == 1:
        return search1(a, x)
    i = 0
    while i < len(a):
        if a[i] == x:
            return i
        i += (abs(a[i] - x) - 1) // k + 1
    return -1

def search1(a, x):
    i = 0
    while i < len(a):
        if a[i] == x:
            return i
        i += abs(a[i] - x)
    return -1
    
a = [8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]
print(search1(a, 3))
a = [2, 4, 5, 7, 7, 6]
print(search(a, 6, 2))