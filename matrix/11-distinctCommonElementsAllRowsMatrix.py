'''
Given a n x n matrix. The problem is to find all the distinct elements common to all rows of the matrix. 
The elements can be printed in any order.

Examples: 

Input : mat[][] = {  {2, 1, 4, 3},
                     {1, 2, 3, 2},  
                     {3, 6, 2, 3},  
                     {5, 2, 5, 3}  }
Output : 2 3

Input : mat[][] = {  {12, 1, 14, 3, 16},
                     {14, 2, 1, 3, 35},  
                     {14, 1, 14, 3, 11},  
                     {14, 25, 3, 2, 1},
                     {1, 18, 3, 21, 14}  }
Output : 1 3 14
'''
from matrix import printS

def findDistinctCommonElements(m):
    resultSet = set()
    firstRowSet = None
    for i in range(len(m)):
        if i == 0:
            firstRowSet = set(m[i])
        else:
            for key in m[i]:
                if key in firstRowSet:
                    resultSet.add(key)
            firstRowSet = resultSet
            resultSet = set()
    return firstRowSet

mat = [[2, 1, 4, 3],
       [1, 2, 3, 2],
       [3, 6, 2, 3],
       [5, 2, 5, 3]]
 
print(findDistinctCommonElements(mat))