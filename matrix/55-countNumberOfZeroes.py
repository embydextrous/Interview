# https://www.geeksforgeeks.org/count-zeros-in-a-row-wise-and-column-wise-sorted-matrix/
# Also see, https://www.geeksforgeeks.org/count-negative-numbers-in-a-column-wise-row-wise-sorted-matrix/

'''
Given a N x N binary matrix (elements in matrix can be either 1 or 0) where each row and column of the matrix 
is sorted in ascending order, count number of 0s present in it.
Expected time complexity is O(N).
Examples: 
 

Input: 
[0, 0, 0, 0, 1]
[0, 0, 0, 1, 1]
[0, 1, 1, 1, 1]
[1, 1, 1, 1, 1]
[1, 1, 1, 1, 1]

Output: 8
'''
def countZeroes(M):
    R, C = len(M), len(M[0])
    i, j = 0, C - 1
    count = 0
    while j >= 0 and i < R:
        if M[i][j] == 0:
            count += j + 1
            i += 1
        else:
            j -= 1
    return count

M = [[0, 0, 0, 0, 1],
       [0, 0, 0, 1, 1],
       [0, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]]
print(countZeroes(M))