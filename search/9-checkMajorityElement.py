# For unsorted array use map
def hasMajorityElement(a):
    n = len(a)
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        if d[i] == (n + 1) // 2:
            return True
    return False

def findLeft(a, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == x and (m == l or a[m-1] != x):
        return m
    if x <= a[m]:
        return findLeft(a, l, m - 1, x)
    return findLeft(a, m + 1, r, x)

def findRight(a, l, r, x):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == x and (m == r or a[m+1] != x):
        return m
    if x >= a[m]:
        return findRight(a, m + 1, r, x)
    return findRight(a, l, m - 1, x)

def checkMajorElement(a):
    n = len(a)
    x = a[n//2]
    l = 0
    r = n - 1
    return count(a, x) >= (n + 1) // 2

# Also see, https://www.geeksforgeeks.org/count-1s-sorted-binary-array/
# Also see, https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/
def count(a, x):
    n = len(a)
    return findRight(a, 0, n - 1, x) - findLeft(a, 0, n - 1, x) + 1

a = [1, 8, 9, 5, 1]
print(hasMajorityElement(a))

a = [0, 0, 1, 1, 1, 1, 2, 2]
print(checkMajorElement(a))
