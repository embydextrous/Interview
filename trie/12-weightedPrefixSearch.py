'''
Given n strings and a weight associated with each string. The task is to find the maximum weight
of string having the given prefix. Print “-1” if no string is present with given prefix.
Examples: 
 

Input : 
s1 = "geeks", w1 = 15
s2 = "geeksfor", w2 = 30
s3 = "geeksforgeeks", w3 = 45
prefix = geek
Output : 45

All the string contain the given prefix, but
maximum weight of string is 45 among all.
'''
from trie import charToIndex

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.weight = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, weight):
        p = self.root
        for c in word:
            index = charToIndex(c)
            if p.children[index] is None:
                p.children[index] = TrieNode()
            p.children[index].weight = max(p.weight, weight)
            p = p.children[index]
        
    def findMaxWeight(self, prefix):
        p = self.root
        for c in prefix:
            index = charToIndex(c)
            if p.children[index] is None:
                return -1
            p = p.children[index]
        return p.weight

trie = Trie()
trie.insert("geeks", 15)
trie.insert("geeksfor", 30)
trie.insert("geeksforgeeks", 45)
trie.insert("geek", 60)


print(trie.findMaxWeight("geek"))