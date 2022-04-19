'''
Given a dictionary of words and an input string, find the longest prefix of the string which is also a word 
in dictionary.

Examples:

Let the dictionary contains the following words:
{are, area, base, cat, cater, children, basement}

Below are some input/output examples:
--------------------------------------
Input String            Output
--------------------------------------
caterer                 cater
basemexy                base
child                   < Empty >
'''
# 1. Create Trie
# 2. Search for word. The point at which search ends will be longest prefix.
from trie import Trie, charToIndex

class Solution:
    def __init__(self, words):
        self.trie = Trie(26)
        for word in words:
            self.trie.insert(word)

    def query(self, key):
        idx = -1
        p = self.trie.root
        for i in range(len(key)):
            index = charToIndex(key[i])
            if p.children[index] is None:
                break
            if p.children[index].isEndOfWord:
                idx = i
            p = p.children[index]
        if idx == -1:
            return "<EMPTY>"
        return key[:idx+1]
            
words = ["are", "area", "base", "cat", "cater", "children", "basement"]
keys = ["caterer", "basemexy", "child"]

s = Solution(words)
for key in keys:
    print(s.query(key))

