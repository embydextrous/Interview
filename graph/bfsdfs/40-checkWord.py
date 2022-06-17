'''
Given a 2D grid of characters and a word, the task is to check if that word exists in the grid or not. A word can be matched in 4 directions at any point.
The 4 directions are Horizontally Left and Right, Vertically Up and Down. 
Examples: 
 

Input:  grid[][] = {"axmy",
                    "bgdf",
                    "xeet",
                    "raks"};
Output: Yes

a x m y
b g d f
x e e t
r a k s

Input: grid[][] = {"axmy",
                   "brdf",
                   "xeet",
                   "rass"};
Output : No
'''
from collections import deque

ROW = [0, -1, 0, 1]
COL = [-1, 0, 1, 0]

# Time Complexity - O(R * C * 4^s)
def isSafe(R, C, x, y):
    return x >= 0 and y >= 0 and x < R and y < C

def checkWordUtil(M, R, C, word, i, j, idx, visited):
    if idx == len(word) - 1:
        return True
    visited[i][j] = True
    result = False
    for k in range(4):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(R, C, x, y) and not visited[x][y] and M[x][y] == word[idx+1]:
            result = checkWordUtil(M, R, C, word, x, y, idx + 1, visited)
            if result == True:
                visited[i][j] = False
                return True
    visited[i][j] = False
    return result

def checkWord(M, word):
    R, C = len(M), len(M[0])
    visited = [[False for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if M[i][j] == word[0]:
                if checkWordUtil(M, R, C, word, i, j, 0, visited):
                    print(f"Pattern found at ({i}, {j})")

M = ["GEEKSFORGEEKS",
     "GEEKSQUIZGEEK",
     "IDEQAPRACTICE"]

word = "GEEKS"
print(checkWord(M, word))