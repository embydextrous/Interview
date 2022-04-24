'''
Given an array of words find the most occurring word in it
Examples: 
 

Input : arr[] = {"geeks", "for", "geeks", "a", 
                "portal", "to", "learn", "can",
                "be", "computer", "science", 
                 "zoom", "yup", "fire", "in", 
                 "be", "data", "geeks"}
Output : geeks 
"geeks" is the most frequent word as it 
occurs 3 times
'''
from trie import charToIndex

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endCount = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.mostFrequentWord = None
        self.maxFrequency = 0

    def insert(self, word):
        p = self.root
        for c in word:
            index = charToIndex(c)
            if p.children[index] is None:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.endCount += 1
        if p.endCount > self.maxFrequency:
            self.maxFrequency = p.endCount
            self.mostFrequentWord = word

def findMostFrequentWord(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return f"The most frequent word is {trie.mostFrequentWord} which occurs {trie.maxFrequency} times in the array."

words = ["geeks", "for", "geeks", "a", 
                "portal", "to", "learn", "can",
                "be", "computer", "science", 
                 "zoom", "yup", "fire", "in", 
                 "be", "data", "geeks"]
print(findMostFrequentWord(words))