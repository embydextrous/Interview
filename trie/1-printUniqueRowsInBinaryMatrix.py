'''
Given a binary matrix, print all unique rows of the given matrix. 

Example: 

Input:
        {0, 1, 0, 0, 1}
        {1, 0, 1, 1, 0}
        {0, 1, 0, 0, 1}
        {1, 1, 1, 0, 0}
Output:
    0 1 0 0 1 
    1 0 1 1 0 
    1 1 1 0 0 
Explanation: 
The rows are r1={0, 1, 0, 0, 1}, 
r2={1, 0, 1, 1, 0}, r3={0, 1, 0, 0, 1}, 
r4={1, 1, 1, 0, 0}, As r1 = r3, remove r3
and print the other rows.

Input:
        {0, 1, 0}
        {1, 0, 1}
        {0, 1, 0}
Output:
   0 1 0
   1 0 1
Explanation: 
The rows are r1={0, 1, 0}, 
r2={1, 0, 1}, r3={0, 1, 0} As r1 = r3,
remove r3 and print the other rows.
'''
def printUniqueRows2(M):
    trie = Trie(2)
    for row in M:
        if trie.insert(row):
            print(row)

class TrieNode:
    def __init__(self, alphabetSize):
        self.children = [None] * alphabetSize
        self.isEndOfWord = False

class Trie:
    def __init__(self, alphabetSize):
        self.alphabetSize = alphabetSize
        self.root = TrieNode(alphabetSize)

    # returns false if already exists
    def insert(self, word):
        p = self.root
        for c in word:
            if p.children[c] == None:
                p.children[c] = TrieNode(self.alphabetSize)
            p = p.children[c]
        if p.isEndOfWord:
            return False
        p.isEndOfWord = True
        return True

M =     [ [ 0, 1, 0, 0, 1 ],
          [ 1, 0, 1, 1, 0 ],
          [ 0, 1, 0, 0, 1 ],
          [ 1, 0, 1, 0, 0 ] ]

printUniqueRows2(M)


