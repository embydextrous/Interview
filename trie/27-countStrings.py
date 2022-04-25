'''
https://www.geeksforgeeks.org/count-of-strings-whose-prefix-match-with-the-given-string-to-a-given-length-k/

Given an array of strings arr[] and given some queries where each query consists of a string str and an 
integer k. The task is to find the count of strings in arr[] whose prefix of length k matches with the k
length prefix of str.
Examples: 
 

    Input: arr[] = {"abba", "abbb", "abbc", "abbd", "abaa", "abca"}, str = "abbg", k = 3 
    Output: 4 
    "abba", "abbb", "abbc" and "abbd" are the matching strings.
    Input: arr[] = {"geeks", "geeksforgeeks", "forgeeks"}, str = "geeks", k = 2 
    Output: 2 
'''
from trie import charToIndex

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        p.count += 1
        for c in word:
            index = charToIndex(c)
            if p.children[index] is None:
                p.children[index] = TrieNode()
            p = p.children[index]
            p.count += 1
        p.isEndOfWord = True

def countWordWithPrefix(words, prefix, k):
    trie = Trie()
    for word in words:
        trie.insert(word)
    p = trie.root
    for i in range(k):
        index = charToIndex(prefix[i])
        if p.children[index] is None:
            return 0
        p = p.children[index]
    return p.count

words = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]
prefix = "abbg"
k = 4
print(countWordWithPrefix(words, prefix, k))