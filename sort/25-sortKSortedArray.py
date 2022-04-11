'''
Given an array of n elements, where each element is at most k away from its target position, 
devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an 
element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

Examples: 

Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}

Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
'''
import heapq
from random import randint

# 6, 5, 3, 2, 8, 10, 9
def sort(a, k):
    n = len(a)
    h = a[:k + 1]
    heapq.heapify(h)
    for i in range(k + 1, n):
        a[i - k - 1] = h[0]
        heapq.heapreplace(h, a[i])
    for i in range(k+1):
        a[n-k-1+i] = heapq.heappop(h)

a = [6, 5, 5, 2, 5, 4, 10, 8, 11, 10, 6, 9, 12, 12, 11]
k = 5
sort(a, k)
print(a)
