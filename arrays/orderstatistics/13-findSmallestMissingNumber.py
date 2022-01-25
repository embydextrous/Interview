# https://www.geeksforgeeks.org/find-the-first-missing-number/

def findSmallestMissingNumber(a):
    return findSmallestUtil(a, 0, len(a) - 1)

def findSmallestUtil(a, l, r):
    if l > r:
        return len(a)
    mid = (l + r ) // 2
    if mid > 0 and a[mid] > mid and a[mid-1] == mid - 1:
        return mid
    if a[mid] == mid:
        return findSmallestUtil(a, mid + 1, r)
    return findSmallestUtil(a, l, mid - 1)

a = [0]
print(findSmallestMissingNumber(a))

