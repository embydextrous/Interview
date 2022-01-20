# https://www.geeksforgeeks.org/difference-maximum-sum-minimum-sum-n-m-elementsin-review/
import heapq

def kLargestElements(a, k):
    h = a[:k]
    heapq.heapify(h)
    for i in range(k, len(a)):
        if a[i] > h[0]:
            h[0] = a[i]
            heapq.heapify(h)
    return h

def kSmallestElements(a, k):
    h = [a[i] * -1 for i in range(k)]
    heapq.heapify(h)
    for i in range(k, len(a)):
        if -1 * a[i] > h[0]:
            h[0] = -1 * a[i]
            heapq.heapify(h)
    return [-1 * h[i] for i in range(k)]

def maxDifference(a, m):
    mSmallestSet = kSmallestElements(a, m)
    mLargestSet = kLargestElements(a, m)
    diff = 0
    for i in range(m):
        diff += mLargestSet[i] - mSmallestSet[i]
    return diff

a = [5, 8, 11, 40, 15]
print(maxDifference(a, 2))