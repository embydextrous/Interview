from heapq import heapify, heappush, heapreplace

def maxFromSubArraysOfSizeK(a, k):
    h = [-1 * a[i] for i in range(k)]
    heapify(h)
    n = len(a)
    for i in range(k, n):
        print(-1 * h[0], end = " ")
        if -h[0] < a[i]:
            heapreplace(h, -a[i])
        else:
            heappush(h, -a[i])
    print(-h[0])

a = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
maxFromSubArraysOfSizeK(a, 4)
