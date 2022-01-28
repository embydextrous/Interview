def findPivot(a, l, r):
    if l > r:
        return a[-1]
    mid = (l + r) // 2
    if mid < r and a[mid+1] < a[mid]:
        return a[mid]
    if mid > l and a[mid-1] > a[mid]:
        return a[mid - 1]
    if a[l] > a[mid]:
        return findPivot(a, l, mid - 1)
    return findPivot(a, mid + 1, r)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(a)
print(findPivot(a, 0, n - 1))