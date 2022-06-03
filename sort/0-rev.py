
# 12, 13, 14, 15, 16, 17, 18, 19, 20
from math import ceil

def count(a, k):
    target = a[0]
    c = 0
    for i in range(1, len(a)):
        x = a[i]
        print(x, target, c)
        if x <= target:
            continue
        else:
            t = ceil((x - target) / k)
            target = x - k * t
            c += t
    return c

a = [1, 8, 10, 6, 9, 12]
print(count(a, 3))