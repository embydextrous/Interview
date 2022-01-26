import sys

def minDifferencePair(a):
    a.sort()
    minDiff = sys.maxsize
    for i in range(1, len(a)):
        minDiff = min(minDiff, a[i] - a[i-1])
    return minDiff

a = [1, 19, -4, 31, 38, 25, 100]
print(minDifferencePair(a))
