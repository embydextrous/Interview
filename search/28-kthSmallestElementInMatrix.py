# https://www.geeksforgeeks.org/kth-smallest-element-in-a-row-wise-and-column-wise-sorted-2d-array-set-1/

'''
Given an n x n matrix, where every row and column is sorted in non-decreasing order. 
Find the kth smallest element in the given 2D array.
Example, 

Input:k = 3 and array =
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50 
Output: 20

Input:k = 7 and array =
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50 
Output: 30
'''
import heapq

def kthSmallest(M, k):
    R, C = len(M), len(M[0])
    h = []
    for i in range(R):
        h.append(HeapNode(M[i][0], i, 0))
    heapq.heapify(h)
    while k > 0:
        node = h[0]
        k -= 1
        if k == 0:
            return node.data
        i, j = node.i, node.j
        if j + 1 < C:
            heapq.heapreplace(h, HeapNode(M[i][j+1], i, j + 1))
        else:
            heapq.heappop(h)


class HeapNode:
    def __init__(self, data, i, j):
        self.data = data
        self.i = i
        self.j = j

    def __lt__(self, other):
        return self.data < other.data

k = 14 
M = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [24, 29, 37, 48],
        [32, 33, 39, 50]] 

print(kthSmallest(M, k))