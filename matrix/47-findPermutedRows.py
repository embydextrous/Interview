'''
We are given an m*n matrix of positive integers and a row number. The task is to find all rows in given 
matrix which are permutations of given row elements. It is also given that values in every row are distinct.

Examples:  

Input : mat[][] = {{3, 1, 4, 2}, 
                   {1, 6, 9, 3},
                   {1, 2, 3, 4},
                   {4, 3, 2, 1}}
        row = 3    
Output: 0, 2
Rows at indexes 0 and 2 are permutations of
row at index 3. 
'''

def findPermutedRows(M, r):
    s = set(M[r])
    p = []
    for i in range(len(M)):
        if i != r:
            isPermutation = True
            for j in range(len(M[0])):
                if M[i][j] not in s:
                    isPermutation = False
            if isPermutation:
                p.append(i)
    return p
            
M =   [[3, 1, 4, 2],
       [1, 6, 9, 3],
       [1, 2, 3, 4],
       [4, 3, 2, 1]]

print(findPermutedRows(M, 3))