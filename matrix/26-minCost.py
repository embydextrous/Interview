# https://www.geeksforgeeks.org/minimum-cost-sort-matrix-numbers-0-n2-1/

'''
Given an n x n matrix containing all the numbers in the range 0 to n2-1. The problem is to calculate the 
total energy required for rearranging all the numbers in the matrix in strictly increasing order, i.e., 
after the rearrangement, the 1st row contains n numbers from 0 to n-1, then 2nd row from n to 2n-1, and so 
on up to the last or nth row. A number can be moved in any of the four directions left, right, top, or bottom
from its current position to reach its destination in the final modified matrix. The number of steps moved 
in transferring a number from its current location to its required destination is the energy required by the
number for its movement. For example, in a 4 x 4 matrix, the number '6' is present at location (2, 3). 
Its destination location in the modified matrix is (1, 1). So '6' is moved 2 steps towards left and 1 step 
up to reach location (1, 1). Total 3 steps moved and thus the energy required by '6' is 3 units. 
In this way, we have to sum up all the energies required in the movement/rearrangement of all the numbers.
'''

def minCostForSorting(M):
    n = len(M)
    cost = 0
    for i in range(n):
        for j in range(n):
            key = M[i][j]
            x, y = key // n, key % n
            cost += abs(x-i) + abs(y-j)
    return cost

M = [[4, 7, 0, 3], # 6
     [8, 5, 6, 1], # 4
     [9, 11, 10, 2], # 6
     [15, 13, 14, 12]] # 6

print(minCostForSorting(M))