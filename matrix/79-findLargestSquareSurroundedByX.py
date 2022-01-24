# https://www.geeksforgeeks.org/given-matrix-o-x-find-largest-subsquare-surrounded-x/
from matrix import printS

def findLargestSubsquare(M):
    R, C = len(M), len(M[0])
    H = [[0 for i in range(C)] for j in range(R)]
    V = [[0 for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                H[i][j] = 1 if M[i][j] == 'X' else 0
                V[i][j] = 1 if M[i][j] == 'X' else 0
            elif i == 0:
                H[i][j] = 1 + H[i][j-1] if M[i][j] == 'X' else 0
                V[i][j] = 1 if M[i][j] == 'X' else 0
            elif j == 0:
                H[i][j] = 1 if M[i][j] == 'X' else 0
                V[i][j] = 1 + V[i-1][j] if M[i][j] == 'X' else 0
            else:
                if M[i][j] == 'X':
                    H[i][j] = 1 + H[i][j-1]
                    V[i][j] = 1 + V[i-1][j]
                else:
                    H[i][j] = 0
                    V[i][j] = 0
    maxSquare = 0
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            x = min(H[i][j], V[i][j])
            while x > max(1, maxSquare):
                firstRowIndex = i - x + 1 
                firstColumnIndex = j - x + 1
                # Check Rows of first row
                loopBroken = False
                for k in range(firstColumnIndex, j):
                    if V[firstRowIndex][k] == 0:
                        x -= 1
                        loopBroken = True
                        break
                if loopBroken:
                    continue
                # Check Columns
                for k in range(firstRowIndex, i):
                    if H[k][firstColumnIndex] == 0:
                        x -= 1
                        loopBroken = True
                        break
                if not loopBroken:
                    break
            maxSquare = max(x, maxSquare)
    return maxSquare

mat = [['X', 'O', 'X', 'X', 'X', 'X'],
       ['X', 'O', 'X', 'X', 'O', 'X'],
       ['X', 'X', 'X', 'O', 'O', 'X'],
       ['O', 'X', 'X', 'X', 'X', 'X'],
       ['X', 'X', 'X', 'O', 'X', 'O'],
       ['O', 'O', 'X', 'O', 'O', 'O']]

print(findLargestSubsquare(mat))



