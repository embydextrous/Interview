# 29
# 33 37 39 40
# 44 45 46 48 49
# 51
from collections import defaultdict
from math import sqrt, ceil

def trappedWater(a):
    l = 0
    r = len(a) - 1
    w = 0
    lMax = rMax = 0
    while l <= r:
        if lMax <= rMax:
            w += max(0, lMax - a[l])
            lMax = max(lMax, a[l])
            l += 1
        else:
            w += max(0, rMax - a[r])
            rMax = max(rMax, a[r])
            r -= 1
    return w

'''
[3, 0r, 4l, 0, 2]
lMax = 3
rMax = 4
w = 5
'''

a = [3, 0, 4, 0, 2]
print(trappedWater(a))
