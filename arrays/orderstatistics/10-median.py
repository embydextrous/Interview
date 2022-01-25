from random import randint

def randomPartition(a, l, r):
    n = r - l + 1
    x = randint(1, 100) % n
    a[r], a[l+x] = a[l+x], a[r]
    return partition(a, l, r)

def partition(a, l, r):
    x = a[r]
    i = l
    for j in range(l, r):
        if a[j] <= x:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

def findMedianUtil(a, l, r, k):
    n = r - l + 1
    if k >= 0 and k < n:
        pos = partition(a, l, r)
        if pos - l == k:
            return a[pos]
        if pos - l > k:
            return findMedianUtil(a, l, pos - 1, k)
        return findMedianUtil(a, pos + 1, r, k - pos + l - 1)

def findMedian(a):
    n = len(a)
    if n % 2 == 1:
        return findMedianUtil(a, 0, n - 1, n // 2)
    else:
        return (findMedianUtil(a, 0, n - 1, n // 2 - 1) + findMedianUtil(a, 0, n - 1, n // 2)) / 2

arr = [2, 1, 9, 6, 8, 4, 5, 7]
print(findMedian(arr))    