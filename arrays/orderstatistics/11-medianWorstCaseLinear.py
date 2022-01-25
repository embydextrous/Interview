def partition(a, l, r, median):
    for i in range(l, r):
        if a[i] == median:
            a[i], a[r] = a[r], a[i]
            break
    i = l
    for j in range(l, r):
        if a[j] <= median:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[r], a[i] = a[i], a[r]
    return i

def findMedian(a, l, n):
    lis = [a[i] for i in range(l, l+n)]
    lis.sort()
    return lis[n//2]

def medianUtil(a, l, r, k):
    n = r - l + 1
    if k >= 0 and k < n:
        medians = []
        i = 0
        while i < n // 5:
            medians.append(findMedian(a, l + i * 5, 5))
            i += 1
        if i * 5 < n:
            medians.append(findMedian(a, l + i * 5, n % 5))
            i += 1
        if i == 1:
            medianOfMedians = medians[i-1]
        else:
            medianOfMedians = medianUtil(medians, 0, i - 1, i // 2)
        pos = partition(a, l, r, medianOfMedians)
        if pos - l == k:
            return a[pos]
        if pos - l > k:
            return medianUtil(a, l, pos - 1, k)
        return medianUtil(a, pos + 1, r, k - pos + l - 1)

def getMedian(a):
    n = len(a)
    if n % 2 == 1:
        return medianUtil(a, 0, n-1, n//2)
    else:
        return (medianUtil(a, 0, n-1, n//2 - 1) + medianUtil(a, 0, n - 1, n//2)) / 2

arr = [2, 1, 9, 6, 8, 4, 5, 3]
# 1 2 4 5 6 8 9
print(getMedian(arr))
