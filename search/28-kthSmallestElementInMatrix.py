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
        heapq.heappush(h, [M[i][0], i, 0])
    while len(h) > 0:
        x, row, col = heapq.heappop(h)
        k -= 1
        if k == 0:
            return x
        if col + 1 < C:
            heapq.heappush(h, [M[row][col + 1], row, col + 1])
    return None


k = 7 
M = [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [24, 29, 37, 48],
        [32, 33, 39, 50]] 

print(kthSmallest(M, k))