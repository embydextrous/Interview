'''
Given an array and an integer k, traverse the array and if the element in array is k, 
double the value of k and continue traversal. In the end return value of k.
Examples: 

Input : arr[] = { 2, 3, 4, 10, 8, 1 }, k = 2
Output: 16
Explanation:
First k = 2 is found, then we search for 4
which is also found, then we search for 8
which is also found, then we search for 16.
 
Input : arr[] = { 2, 4, 5, 6, 7 }, k = 3
Output: 3
'''
from search import binarySearchUtil

def finalValue(a, k):
    a.sort()
    l = 0
    r = len(a) - 1
    while l <= r:
        if a[r] < k:
            return k
        idx = binarySearchUtil(a, l, r, k)
        if  idx == -1:
            return k
        k *= 2
        l = idx + 1

# 1 2 3 4 8 10
# k = 2
a = [2, 3, 4, 10, 8, 1]
k = 1
print(finalValue(a, 2))