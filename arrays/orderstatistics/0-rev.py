from collections import deque
from heapq import heapify, heappop, heapreplace, heappush
from random import randint

def partition(a, l, r, median):
    for i in range(l, r):
        if a[i] == median:
            a[r], a[i] = a[i], a[r]
            break
    i = l
    for j in range(l, r):
        if a[j] <= a[r]:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

def findMedian(a, l, r):
    lst = [a[i] for i in range(l, r + 1)]
    n = (r - l + 1)
    return lst[n // 2]

def medianUtil(a, l, r, k):
    if l <= r and k - 1 >= l and k - 1 <= r:
        median = []
        i = l
        while i + 4 <= r:
            median.append(findMedian(a, i, i + 4))
            i += 5
        if i <= r:
            median.append(findMedian(a, i, r))
        if len(median) == 1:
            medianOfMedians = median[0]
        else:
            medianOfMedians = medianUtil(median, 0, len(median) - 1, len(median) // 2 + 1)
        p = partition(a, l, r, medianOfMedians)
        if p == k - 1:
            return a[p]
        if p < k - 1:
            return medianUtil(a, p + 1, r, k)
        return medianUtil(a, l, p - 1, k)

def getMedian(a):
    n = len(a)
    if n % 2 == 1:
        return medianUtil(a, 0, n - 1, n // 2 + 1)
    else:
        return (medianUtil(a, 0, n - 1, n // 2 + 1) + medianUtil(a, 0, n - 1, n // 2)) / 2.0

# [1, 3, 4, 6, 9, 11, 15, 19, 13]

# 1 2 4 5
# 0 3 5 8  
a = [randint(1, 20) for i in range(34)]
print(sorted(a))
print(getMedian(a))

    

