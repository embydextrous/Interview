'''
Given a dictionary, a method to do a lookup in the dictionary and a M x N board where every cell has 
one character. Find all possible words that can be formed by a sequence of adjacent characters. Note 
that we can move to any of 8 adjacent characters, but a word should not have multiple instances of the same cell.
Example: 
 

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G', 'I', 'Z'},
                       {'U', 'E', 'K'},
                       {'Q', 'S', 'E'}};

Output: Following words of the dictionary are present
         GEEKS
         QUIZ
'''
from trie import Trie
from collections import defaultdict

def charToIndex(c):
    return ord(c) - ord('A')

def indexToChar(i):
    return chr(i + ord('A'))


ROW = [0, -1, -1, -1, 0, 1, 1, 1]
COL = [-1, -1, 0, 1, 1, 1, 0, -1]

def isReachable(x, y, i, j):
    for k in range(8):
        if x + ROW[k] == i and y + COL[k] == j:
            return True
    return False

def findWordsUtil(root, board, R, C, positionMap, lastPosition, prefix, visited):
    if root.isEndOfWord:
        print(prefix)
    visited.add(lastPosition)
    (x, y) = lastPosition
    for i in range(len(root.children)):
        if root.children[i] is not None:
            for (p, q) in positionMap[indexToChar(i)]:
                if isReachable(x, y, p, q) and (p, q) not in visited:
                    findWordsUtil(root.children[i], board, R, C, positionMap, (p, q), prefix + indexToChar(i), visited)
                    visited.remove((p, q))

def findWords(words, board):
    trie = Trie(26, charToIndex)
    for word in words:
        trie.insert(word)
    positionMap = {}
    R, C = len(board), len(board[0])
    positionMap = defaultdict(set)
    for i in range(R):
        for j in range(C):
            positionMap[board[i][j]].add((i, j))
    for i in range(len(trie.root.children)):
        if trie.root.children[i] is not None:
            for (x, y) in positionMap[indexToChar(i)]:
                visited = set()
                findWordsUtil(trie.root.children[i], board, R, C, positionMap, (x, y), indexToChar(i), visited)

words = ["GEEKS", "FOR", "QUIZ", "GO"]
board = [['G', 'I', 'Z'],
        ['U', 'E', 'K'],
        ['Q', 'S', 'E']]

findWords(words, board)