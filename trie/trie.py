ALPHABET_SIZE = 26

class TrieNode:
    def __init__(self, alphabetSize):
        self.children = [None] * alphabetSize
        self.setChildCount = 0
        self.count = 0
        self.isEndOfWord = False

class Trie:
    def __init__(self, alphabetSize):
        self.alphabetSize = alphabetSize
        self.root = TrieNode(alphabetSize)

    def charToIndex(self, c):
        return ord(c) - ord('a')

    # Time Complexity - O(length of string)
    def insert(self, key):
        pCrawl = self.root
        for c in key:
            index = self.charToIndex(c)
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode(self.alphabetSize)
                pCrawl.setChildCount += 1
            pCrawl = pCrawl.children[index]
            pCrawl.count += 1
        pCrawl.isEndOfWord = True

    # Time Complexity - O(length of string)
    def search(self, key):
        pCrawl = self.root
        for c in key:
            index = self.charToIndex(c)
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord