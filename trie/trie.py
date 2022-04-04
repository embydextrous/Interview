ALPHABET_SIZE = 26

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, c):
        return ord('c') - ord('a')

    # Time Complexity - O(length of string)
    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self.charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    # Time Complexity - O(length of string)
    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self.charToIndex(key[level])
            if pCrawl.children[index] == None:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord