# Also see, https://www.geeksforgeeks.org/trie-memory-optimization-using-hash-map/
class TrieNode:
    def __init__(self, alphabetSize):
        self.children = [None] * alphabetSize
        self.childCount = 0
        self.visitCount = 0
        self.isEndOfWord = False
        self.data = None

    def __str__(self) -> str:
        return f"{self.children}"

def charToIndex(c):
    return ord(c) - ord('a')

def indexToChar(i):
    return chr(ord('a') + i)

class Trie:
    def __init__(self, alphabetSize, cToI = None):
        self.alphabetSize = alphabetSize
        self.charToIndex = cToI if cToI is not None else charToIndex
        self.root = TrieNode(alphabetSize)

    def insert(self, key):
        p = self.root
        for c in key:
            index = self.charToIndex(c)
            if p.children[index] is None:
                p.children[index] = TrieNode(self.alphabetSize)
                p.childCount += 1
            p = p.children[index]
            p.visitCount += 1
        p.isEndOfWord = True

    def insertWithData(self, key, data):
        p = self.root
        for c in key:
            index = self.charToIndex(c)
            if p.children[index] is None:
                p.children[index] = TrieNode(self.alphabetSize)
                p.childCount += 1
            p = p.children[index]
            p.visitCount += 1
        p.data = data

    def search(self, key):
        p = self.root
        for c in key:
            index = charToIndex(c)
            if p.children[index] is None:
                return False
            p = p.children[index]
        return p.isEndOfWord
