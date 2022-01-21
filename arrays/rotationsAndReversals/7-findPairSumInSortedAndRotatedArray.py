def findPairSum(a, s):
    n = len(a)
    pivot = findPivot(a, 0, n - 1)
    l, r = pivot + 1, pivot % n # Mod N if pivot is -1
    while l != r:
        if a[l] + a[r] == s:
            return (l, r)
        if a[l] + a[r] < s:
            l = (l + 1) % n
        else:
            r = (r - 1) % n
    return (-1, -1)

def findPivot(a, l, r):
    if l > r:
        return -1
    m = (l + r) // 2
    if m < r and a[m+1] < a[m]:
        return m
    if m > l and a[m-1] >  a[m]:
        return m - 1
    if a[l] > a[m]:
        return findPivot(a, l, m - 1)
    return findPivot(a, m + 1, r)

a = [1, 2, 3, 4, 5, 6, 7, 8]
print(findPairSum(a, 15))
