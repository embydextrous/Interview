def pairSum(a, x):
    n = len(a)
    l, r = 0, len(a) - 1
    pivot = findPivot(a, l, r)
    if (pivot != -1):
        l, r = pivot + 1, pivot
    while l != r:
        if a[l] + a[r] == x:
            return (a[l], a[r])
        elif a[l] + a[r] < x:
            l = (l + 1) % n
        else:
            r = (r - 1) % n
    return [-1, -1]


def findPivot(a, l, r):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if m > l and a[m - 1] > a[m]:
        return m - 1
    if m < r and a[m + 1] < a[m]:
        return m
    if a[m] < a[l]:
        return findPivot(a, l, m - 1)
    return findPivot(a, m + 1, r)

a = [11, 15, 26, 38, 9, 10]
print(pairSum(a, 24))