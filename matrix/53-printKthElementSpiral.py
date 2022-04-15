'''
Given a 2D Matrix of order n X m, print K'th element in the spiral form of the matrix. 

Input: mat[][] = 
          {{1, 2, 3, 4}
           {5, 6, 7, 8}
           {9, 10, 11, 12}
           {13, 14, 15, 16}}
       k = 6
Output: 12
Explanation: The elements in spiral order is 
1, 2, 3, 4, 8, 12, 16, 15...
so the 6th element is 12

Input: mat[][] =
       {{1, 2, 3, 4, 5, 6}
        {7, 8, 9, 10, 11, 12}
        {13, 14, 15, 16, 17, 18}}
       k = 17
Output: 10
Explanation: The elements in spiral order is 
1, 2, 3, 4, 5, 6, 12, 18, 17,
16, 15, 14, 13, 7, 8, 9, 10, 11 
so the 17 th element is 10.  
'''
def traverseRing(M, R, C, k, i, count):
    # traverse top row
    for j in range(i, C - i):
        x = M[i][j]
        count[0] += 1
        if count[0] == k:
            print(x)
            return
    # traverse right column
    for j in range(i + 1, R - i):
        x = M[j][C-i-1]
        count[0] += 1
        if count[0] == k:
            print(x)
            return

    # traverse bottom row
    for j in range(C-i-2, i-1, -1):
        x = M[R-i-1][j]
        count[0] += 1
        if count[0] == k:
            print(x)
            return

    # traverse left edge
    for j in range(R-i-2, i, -1):
        x = M[j][i]
        count[0] += 1
        if count[0] == k:
            print(x)
            return

def printKthElement(M, k):
    R, C = len(M), len(M[0])
    to = min(R + 1, C + 1) // 2
    count = [0]
    for i in range(to):
        traverseRing(M, R, C, k, i, count)
        if count[0] == k:
            return

M = [[1, 2, 3, 4, 5, 6 ],
    [ 7, 8, 9, 10, 11, 12 ],
    [ 13, 14, 15, 16, 17, 18]]
k = 3
for i in range(1, 19):
    printKthElement(M, i)