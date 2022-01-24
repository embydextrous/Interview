# https://www.geeksforgeeks.org/print-elements-sorted-order-row-column-wise-sorted-matrix/
import heapq
from operator import index

def printElements(M):
    R, C = len(M), len(M[0])
    h = [M[i][0] for i in range(R)]
    indexes = [0 for i in range(R)]
    heapq.heapify(h)
    while len(h) > 0:
        x = heapq.heappop(h)
        print(x, end = " ")
        for i in range(R):
            if indexes[i] < C and M[i][indexes[i]] == x:
                indexes[i] += 1
                if indexes[i] < C:
                    heapq.heappush(h, M[i][indexes[i]])
                break
    print()

M =   [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

printElements(M)
