'''
Given a matrix where every row is sorted in increasing order. Write a function that finds and returns a 
common element in all rows. If there is no common element, then returns -1. 
Example: 
 

Input: mat[4][5] = { {1, 2, 3, 4, 5},
                    {2, 4, 5, 8, 10},
                    {3, 5, 7, 9, 11},
                    {1, 3, 5, 7, 9},
                  };
Output: 5
'''
# Works even if row is not sorted
def findCommonElement(M):
    R, C = len(M), len(M[0])
    common = set()
    p, q = 0, 0
    while p < C and q < C:
        if M[0][p] == M[1][q]:
            common.add(M[0][p])
            p += 1
            q += 1
        elif M[0][p] < M[1][q]:
            p += 1
        else:
            q += 1
    i = 2
    while len(common) > 0 and i < R:
        temp = set()
        for j in range(C):
            if M[i][j] in common:
                temp.add(M[i][j])
        common = temp
        i += 1
    return None if len(common) == 0 else common.pop()

M =    [[1, 2, 3, 4, 5 ],
        [2, 4, 5, 8, 10],
        [1, 5, 7, 9, 11],
        [1, 3, 5, 7, 9 ]]

print(findCommonElement(M))
