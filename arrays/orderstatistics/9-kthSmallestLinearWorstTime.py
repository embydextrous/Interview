def partition(a, l, r, x):
    for i in range(l, r):
        if a[i] == x:
            a[i], a[r] = a[r], a[i]
            break
    i = l
    for j in range(l, r):
        if a[j] <= x:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

def kthSmallest(a, l, r, k):
    n = r - l + 1
    if k - 1 >= l and k - 1 <= r:
        median = []
        i = 0
        while i < n // 5:
            median.append(findMedian(a, l + i * 5, 5))
            i += 1
        if i * 5 < n:
            median.append(findMedian(a, l + i * 5, n % 5))
            i += 1
        if i == 1:
            medianOfMedian = median[i-1]
        else:
            medianOfMedian = kthSmallest(median, 0, i - 1, i // 2)
        pos = partition(a, l, r, medianOfMedian)
        if pos == k - 1:
            return a[pos]
        if pos > k - 1:
            return kthSmallest(a, l, pos - 1, k)
        return kthSmallest(a, pos + 1, r, k)

def findMedian(a, l, n):
    lis = [a[i] for i in range(l, l + n)]
    lis.sort()
    return lis[n//2]

arr = [2, 1, 9, 6, 8, 4, 5, 7]
n = len(arr)
for i in range(n+1):
    print(kthSmallest(arr, 0, n-1, i))
