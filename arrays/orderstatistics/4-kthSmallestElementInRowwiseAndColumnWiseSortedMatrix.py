import heapq
from operator import index

def kthSmallestElement(M, k):
    R, C = len(M), len(M[0])
    indexes = [0] * R
    h = []
    for i in range(R):
        heapq.heappush(h, M[i][0])
    while True:
        x = heapq.heappop(h)
        k -= 1
        if k == 0:
            return x
        for i in range(R):
            if indexes[i] < C and M[i][indexes[i]] == x:
                indexes[i] += 1
                if indexes[i] < C:
                    heapq.heappush(h, M[i][indexes[i]])
                break

M =    [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [25, 29, 37, 48],
        [32, 33, 39, 50]] 

print(kthSmallestElement(M, 14))
