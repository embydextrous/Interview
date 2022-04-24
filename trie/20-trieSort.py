'''
Given an array of strings, print them in alphabetical (dictionary) order.
 
Input : "abc", "xy", "bcd"
Output : abc bcd xy         

Input : "geeks", "for", "geeks", "a", "portal", 
        "to", "learn", "can", "be", "computer", 
        "science", "zoom", "yup", "fire", "in", "data", "geeks"
Output : a be can computer data fire for geeks
         geeks in learn portal science to yup zoom
'''
from trie import charToIndex, indexToChar

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endCount = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for c in word:
            index = charToIndex(c)
            if p.children[index] is None:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.endCount += 1

    def printSortedUtil(self, root, prefix):
        for i in range(root.endCount):
            print("".join(prefix), end = " ")
        for i in range(len(root.children)):
            if root.children[i] is not None:
                char = indexToChar(i)
                prefix.append(char)
                self.printSortedUtil(root.children[i], prefix)
                prefix.pop()

    def printSorted(self):
        prefix = []
        self.printSortedUtil(self.root, prefix)
        print()

def printSorted(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    trie.printSorted()

words = ["geeks", "for", "geeks", "a", "portal", "bitcoin",
        "to", "learn", "can", "be", "computer", "water", "ethereum", "solana",
        "science", "zoom", "yup", "fire", "in", "data", "geeks"]

printSorted(words)