import heapq

def maxFromSubArraysOfSizeK(a, k):
    h = [-1 * a[i] for i in range(k)]
    heapq.heapify(h)
    n = len(a)
    for i in range(k, n+1):
        print(-1 * h[0], end = " ")
        if i == n:
            break
        enter, exit = -1 * a[i], -1 * a[i - k]
        for j in range(k):
            if h[j] == exit:
                h[j] = enter
                heapq.heapify(h)
                break
    print()

a = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
maxFromSubArraysOfSizeK(a, 4)
