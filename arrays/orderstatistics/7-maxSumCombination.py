from heapq import heappop, heappush

# Similar Question https://www.geeksforgeeks.org/find-k-pairs-smallest-sums-two-arrays/ (We have to find minimum here)

class MaxSumPairNode:
    def __init__(self, sum , i1, i2):
        self.sum = sum
        self.i1 = i1
        self.i2 = i2

    # Doing this for max heap filling
    def __lt__(self, other):
        return (-1 * self.sum) < (-1 * other.sum)

    def __str__(self) -> str:
        return "MaxSumPair(sum={}, i1={}, i2={})".format(self.sum, self.i1, self.i2)

def maxSumCombination(a, b, k):
    n = len(a)
    a.sort()
    b.sort()
    h = [MaxSumPairNode(a[n-1] + b[n-1], n-1, n-1)]
    indexSet = set()
    indexSet.add((n-1, n-1))
    for i in range(k):
        node = heappop(h)
        print(node)
        if node.i1 > 0:
            newNode = MaxSumPairNode(a[node.i1-1] + b[node.i2], node.i1-1, node.i2)
            if (node.i1-1, node.i2) not in indexSet:
                indexSet.add((node.i1-1, node.i2))
                heappush(h, newNode)
        if node.i2 > 0:
            newNode = MaxSumPairNode(a[node.i1] + b[node.i2-1], node.i1, node.i2-1)
            if (node.i1, node.i2-1) not in indexSet:
                indexSet.add((node.i1, node.i2-1))
                heappush(h, newNode)
    
a = [4, 2, 5, 1]
b = [8, 0, 3, 5]
k = 14
maxSumCombination(a, b, k)

# 1 2 4 5
# 0 3 5 8


