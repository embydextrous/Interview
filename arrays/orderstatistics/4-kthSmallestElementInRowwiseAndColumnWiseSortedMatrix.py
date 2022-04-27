import heapq

def kthSmallestElement(M, k):
    R, C = len(M), len(M[0])
    h = []
    for i in range(R):
        heapq.heappush(h, [M[i][0], i, 0])
    while True:
        (ele, row, idx) = heapq.heappop(h)
        k -= 1
        if k == 0:
            return ele
        if idx + 1 < C:
            heapq.heappush(h, [M[row][idx + 1], row, idx + 1])

M =    [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [25, 29, 37, 48],
        [32, 33, 39, 50]] 

print(kthSmallestElement(M, 14))
