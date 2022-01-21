def searchInSortedAndRotatedArray(a, x):
    n = len(a)
    pivot = findPivot(a, 0, n - 1)
    if pivot == -1:
        return binarySearch(a, 0, n - 1, x)
    if a[0] <= x:
        return binarySearch(a, 0, pivot, x)
    return binarySearch(a, pivot + 1, n - 1, x)

def findPivot(a, l, r):
    if l > r:
        return -1
    m = (l + r) // 2
    if m < r and a[m + 1] < a[m]:
        return m
    if m > l and a[m - 1] > a[m]:
        return m - 1
    if a[l] > a[m]:
        findPivot(a, l, m - 1)
    findPivot(a, m + 1, r)

def binarySearch(a, l, r, x):
    if l > r:
        return -1
    m = (l + r) // 2
    if a[m] == x:
        return m
    if a[m] < x:
        return binarySearch(a, m + 1, r, x)
    return binarySearch(a, l, m - 1, x)

a = [4, 5, 6, 7, 1, 2, 3]
print(searchInSortedAndRotatedArray(a, 4))