def findMinElement(a):
    pivot = findPivot(a, 0, len(a) - 1)
    return a[pivot + 1]

def findMaxElement(a):
    return a[findPivot(a, 0, len(a) - 1)]

def findPivot(a, l, r):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if m > l and a[m-1] > a[m]:
        return m - 1 
    if m < r and a[m + 1] < a[m]:
        return m
    if a[m] < a[l]:
        return findPivot(a, l, m - 1)
    return findPivot(a, m + 1, r)

a = [5, 8, 9, 2, 4]
print(findMinElement(a))