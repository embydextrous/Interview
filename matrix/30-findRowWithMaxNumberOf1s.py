# https://www.geeksforgeeks.org/find-row-number-binary-matrix-maximum-number-1s/

'''
Given a binary matrix (containing only 0 and 1) of order nxn. All rows are sorted already, 
We need to find the row number with the maximum number of 1s. Also, find the number of 1 in that row. 
Note: in case of a tie, print the smaller row number.
'''
def findNumOf1(a):
    n = len(a)
    l, r = 0, n - 1 
    while l <= r:
        m = l + (r-l) // 2
        if a[m] == 1 and (m == 0 or a[m-1] == 0):
            return n - m
        if a[m] == 1:
            r = m - 1
        else:
            l = m + 1
    return 0

def rowWithMaxOnes(M):
    maxRowIndex, maxOnes = -1, -1
    for i in range(len(M)):
        numOnes = findNumOf1(M[i])
        if numOnes > maxOnes:
            maxOnes = numOnes
            maxRowIndex = i
    return (maxRowIndex, maxOnes)

M = [[0, 0, 1, 1],
     [1, 1, 1, 1],
     [0, 0, 0, 1],
     [0, 0, 1, 1]]

print(rowWithMaxOnes(M))
