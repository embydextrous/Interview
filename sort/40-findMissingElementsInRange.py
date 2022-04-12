'''
Given an array, arr[0..n-1] of distinct elements and a range [low, high], find all numbers that are in a range, 
but not the array. The missing elements should be printed in sorted order.

Examples:  

Input: arr[] = {10, 12, 11, 15}, 
       low = 10, high = 15
Output: 13, 14

Input: arr[] = {1, 14, 11, 51, 15}, 
       low = 50, high = 55
Output: 50, 52, 53, 54
'''
# Sorting based solution
def printMissing(a, low, high):
    a.sort()
    l = 0
    r = len(a) - 1
    for i in range(low, high + 1):
        idx = binarySearch(a, l, r, i)
        if idx == -1:
            print(i, end = " ")
        else:
            l = idx + 1
    print()

def binarySearch(a, l, r, x):
    if l > r:
        return -1
    m = l + (r-l) // 2
    if a[m] == x:
        return m
    if a[m] > x:
        return binarySearch(a, l, m - 1, x)
    return binarySearch(a, m + 1, r, x)

# Hash Based Solution
def printMissing2(a, low, high):
    exists = [False] * (high - low + 1)
    for i in a:
        if i >= low and i <= high:
            exists[i - low] = True
    for i in range(len(exists)):
        if not exists[i]:
            print(low + i, end = " ")
    print()

a = [10, 12, 11, 15]
low = 10
high = 15
printMissing2(a, low, high)