import sys

# Also, see https://www.geeksforgeeks.org/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/

def findPair(a):
    a.sort()
    l, r = 0, len(a) - 1
    maxSum = sys.maxsize
    x, y = -1, -1
    while l < r:
        if abs(a[l] + a[r]) < maxSum:
            maxSum = a[l] + a[r]
            x, y = a[l], a[r]
        if a[l] + a[r] == 0:
            break
        elif a[l] + a[r] < 0:
            l += 1
        else:
            r -= 1
    return (x, y)

arr = [1, 60, -10, 70, -80, 85]
print(findPair(arr))
