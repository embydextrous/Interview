'''
Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character. Find all possible words that can be formed by a 
sequence of adjacent characters. Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.
Example: 
 

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G', 'I', 'Z'},
                       {'U', 'E', 'K'},
                       {'Q', 'S', 'E'}};
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ
'''
words = set(["GEEKS", "FOR", "QUIZ", "GO"])
board = [['G', 'I', 'Z'],
         ['U', 'E', 'K'],
         ['Q', 'S', 'E']]
R, C = len(board), len(board[0])

def isSafe(x, y):
    return x >= 0 and x < R and y >= 0 and y < C

ROW = [-1, -1, -1, 0, 1, 1, 1, 0]
COL = [-1, 0, 1, 1, 1, 0, -1, -1]

# Time Complexity is O(R*R*C*C)
def search(i, j, currentStr, visited):
    currentStr.append(board[i][j])
    currentWord = "".join(currentStr)
    visited[i][j] = True
    if currentWord in words:
        print(currentWord)
    for k in range(8):
        x, y = i + ROW[k], j + COL[k]
        if isSafe(x, y) and not visited[x][y]:
            search(x, y, currentStr, visited)
    currentStr.pop()
    visited[i][j] = False

def boggle():
    currentStr = []
    visited = [[False for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            search(i, j, currentStr, visited)

boggle()
