from heapq import heappop, heappush, heappushpop

class HeapNode:
    def __init__(self, sum, i, j):
        self.sum = sum
        self.i = i
        self.j = j

    def __lt__(self, other):
        return self.sum < other.sum
    
    def __str__(self) -> str:
        return "HeapNode(sum={}, i={}, j={})".format(self.sum, self.i, self.j)

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
            if len(h) < k:
                heappush(h, HeapNode(subArraySum(preSum, i, j), i, j))
            else:
                x = subArraySum(preSum, i, j)
                if x > h[0].sum:
                    heappop(h)
                    heappush(h, HeapNode(x, i, j))
    return h[0]

a = [10, -10, 20, -40]
print(kthLargestSubArray(a, 6))