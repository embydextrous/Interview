from heapq import heappush, heapreplace

def kthLargestContiguousSumSubArray(a, k):
    i = j = 0
    n = len(a)
    h = []
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            if len(h) < k:
                heappush(h, [sum, i, j])
            else:
                if sum >= h[0][0]:
                    heapreplace(h, [sum, i, j])
    return h[0][0], a[h[0][1]:h[0][2]+1]

a = [10, -10, 20, -40]
print(kthLargestContiguousSumSubArray(a, 2))

# 20 20 10 10 0 -10 -20 -20 -30 -40