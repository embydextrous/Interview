from heapq import heappop, heappush, heappushpop, heapreplace

def subArraySum(preSum, i, j):
    if i == 0:
        return preSum[j]
    return preSum[j] - preSum[i-1]

def kthLargestSubArray(a, k):
    n = len(a)
    preSum = [x for x in a]
    for i in range(1, n):
        preSum[i] += preSum[i-1]
    h = []
    for i in range(n):
        for j in range(i, n):
            subarraysum = subArraySum(preSum, i, j)
            if len(h) < k:
                heappush(h, (subarraysum, i, j))
            else:
                if subarraysum > h[0][0]:
                    heapreplace(h, (subarraysum, i, j))
    return h[0][0]

a = [10, -10, 20, -40]
print(kthLargestSubArray(a, 6))