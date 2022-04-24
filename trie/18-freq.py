'''
You are given a collection of strings and a list of queries. For every query there is a string given. 
We need to print the number of times the given string occurs in the collection of strings. 
Examples: 

Input : arr[] = {wer, wer, tyu, oio, tyu}
        q[] =   {wer, tyu, uio}
Output : 2 2 0
Explanation : 
q[0] appears two times in arr[], q1[] appears
'''
from trie import charToIndex

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.times = 0

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
        p.times += 1

    def frequency(self, word):
        p = self.root
        for c in word:
            index = charToIndex(c)
            if p.children[index] is None:
                return 0
            p = p.children[index]
        return p.times

words = ["wer", "wer", "tyu", "oio", "tyu"]
queries = ["wer", "tyu", "uio"]
trie = Trie()
for word in words:
    trie.insert(word)
for word in queries:
    print(trie.frequency(word))
