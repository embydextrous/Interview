'''
Given a matrix containing lower alphabetical characters only, we need to count number of palindromic paths in given matrix. A path is defined as a sequence of cells starting from top-left cell and ending at bottom-right cell. We are allowed to move to right and down only from current cell. 

Examples: 

Input : mat[][] = {"aaab”, 
                   "baaa”
                   “abba”}
Output : 3

Number of palindromic paths are 3 from top-left to 
bottom-right.
aaaaaa (0, 0) -> (0, 1) -> (1, 1) -> (1, 2) -> 
                                (1, 3) -> (2, 3)    
aaaaaa (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> 
                                (1, 3) -> (2, 3)    
abaaba (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> 
                                 (2, 2) -> (2, 3)    
'''
def numPathsUtil(M, R, C, x1, y1, x2, y2, memo):
    if x1 >= R or y1 >= C or x2 < 0 or y2 < 0:
        return 0
    if M[x1][y1] != M[x2][y2]:
        return 0
    if x1 == x2 and y1 == y2:
        return 1
    if x1 + 1 == x2 and y1 == y2:
        return 1
    if y1 + 1 == y2 and x2 == x1:
        return 1
    if ((x1, x2, y1, y2)) in memo:
        return memo[(x1, x2, y1, y2)]
    result = 0
    result += numPathsUtil(M, R, C, x1 + 1, y1, x2 - 1, y2, memo)
    result += numPathsUtil(M, R, C, x1 + 1, y1, x2, y2 - 1, memo)
    result += numPathsUtil(M, R, C, x1, y1 + 1, x2 - 1, y2, memo)
    result += numPathsUtil(M, R, C, x1, y1 + 1, x2, y2 - 1, memo)
    memo[(x1, x2, y1, y2)] = result
    return result

M = ['aaab',
     'baaa',
     'abba']
R, C = len(M), len(M[0])
memo = {}
numPathsUtil(M, R, C, 0, 0, R - 1, C - 1, memo)
print(memo[(0, R - 1, 0, C - 1)])