# https://www.geeksforgeeks.org/find-the-first-missing-number/

'''
Given a sorted array of n distinct integers where each integer is in the range from 0 to 
m-1 and m > n. Find the smallest number that is missing from the array. 

Examples 

Input: {0, 1, 2, 6, 9}, n = 5, m = 10 
Output: 3

Input: {4, 5, 10, 11}, n = 4, m = 12 
Output: 0

Input: {0, 1, 2, 3}, n = 4, m = 5 
Output: 4

Input: {0, 1, 2, 3, 4, 5, 6, 7, 10}, n = 9, m = 11 
Output: 8
'''

def findSmallestMissing(a, l, r):
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] == m:
        if r > m:
            return findSmallestMissing(a, m + 1, r)
        else:
            return m + 1
    elif a[m] > m:
        if m > l:
            return findSmallestMissing(a, l, m - 1)
        else:
            return m

a = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]
print(findSmallestMissing(a, 0, len(a) - 1))

