def smallestGreaterElement(a):
    n = len(a)
    result = ['_'] * n
    sortedA = sorted(a)
    for i in range(n):
        idx = findKey(sortedA, 0, n-1, a[i])
        if idx >= 0 and idx < n - 1:
            result[i] = sortedA[idx + 1]
    return result

def findKey(a, l, r, x):
    if l > r:
        return -1
    m = (l + r) // 2
    if a[m] == x:
        return m
    if a[m] > x:
        return findKey(a, l, m - 1, x)
    return findKey(a, m + 1, r, x)

a = [6, 3, 9, 8, 10, 2, 1, 15, 7]
print(smallestGreaterElement(a))
