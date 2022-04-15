'''
There is a given binary matrix, we need to find if there exists any rectangle or square in the given matrix 
whose all four corners are equal to 1

Examples: 

Input :
mat[][] = { 1 0 0 1 0
            0 0 1 0 1
            0 0 0 1 0
            1 0 1 0 1}
Output : Yes
as there exists-
1 0 1
0 1 0
1 0 1
'''
def checkIfRectangleWithCornerAsOne(M):
    R, C = len(M), len(M[0])
    d = [set() for i in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                d[i].add(j)
    for i in range(R - 1):
        for j in range(i + 1, R):
            if len(d[i].intersection(d[j])) >= 2:
                print(i, j)
                return True
    return False

M = [[1, 0, 0, 1, 0 ],
     [0, 1, 1, 1, 1 ],
     [0, 0, 0, 1, 0 ],
     [1, 1, 0, 0, 0 ]]

print(checkIfRectangleWithCornerAsOne(M))