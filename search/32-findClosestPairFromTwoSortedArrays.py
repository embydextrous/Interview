import sys

def closestPair(a, b, x):
    l = 0
    r = len(b) - 1
    minDiff = sys.maxsize
    closestPair = None
    while l < len(a) and r >= 0:
        if abs(a[l] + b[r] - x) < minDiff:
            minDiff = abs(a[l] + b[r] - x)
            closestPair = (a[l], b[r])
        if a[l] + b[r] == x:
            return closestPair
        if a[l] + b[r] < x:
            l += 1
        else:
            r -= 1
    return closestPair

a = [1, 4, 5, 7]
b = [10, 20, 30, 40]
x = 38
print(closestPair(a, b, x))