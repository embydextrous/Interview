# https://www.geeksforgeeks.org/minimum-difference-max-min-k-size-subsets/
import sys


# https://www.geeksforgeeks.org/chocolate-distribution-problem/
def minDiff(a, k):
    a.sort()
    n = len(a)
    minDiff = sys.maxsize
    for i in range(n-k+1):
        minDiff = min(minDiff, a[i+k-1] - a[i])
    return minDiff

a = [12, 4,  7,  9,  2,  23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
print(minDiff(a, 7))