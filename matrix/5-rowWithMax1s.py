# https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
'''
Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s. 

Example:  

Input matrix
0 1 1 1
0 0 1 1
1 1 1 1  // this row has maximum 1s
0 0 0 0

Output: 2
'''

def firstIndexOf1InSortedBinaryArray(a, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if a[mid] == 1 and (mid == 0 or a[mid - 1] == 0):
            return mid
        elif a[mid] == 0:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def rowWithMost1s(m):
    n = len(m)
    c = len(m[0]) - 1
    maxIndex, maxIndexRow = c, -1
    for i in range(n):
        first1Index = firstIndexOf1InSortedBinaryArray(m[i], 0, c)
        if first1Index != -1 and first1Index < maxIndex:
            maxIndex, maxIndexRow = first1Index, i
    return maxIndexRow

mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

print("Index of row with maximum 1s is: " + str(rowWithMost1s(mat)))
