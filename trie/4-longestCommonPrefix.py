# https://www.geeksforgeeks.org/longest-common-prefix-using-trie/
'''
Given a set of strings, find the longest common prefix.

Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
Output : "gee"

Input  : {"apple", "ape", "april"}
Output : "ap"
'''
# Needs trie modification to store visit count at each node.
from trie import Trie, charToIndex

def longestCommonPrefix(words):
    N = len(words)
    trie = Trie(26)
    for i in range(N-1):
        trie.insert(words[i])
    lastWord = words[N-1]
    p = trie.root
    for i in range(len(lastWord)):
        index = charToIndex(lastWord[i])
        if p.children[index] is None:
            return lastWord[:i]
        if p.children[index].visitCount < N - 1:
            return lastWord[:i]
        p = p.children[index]
    return lastWord

words = ["apple", "ape", "april", "a"]
print(longestCommonPrefix(words))
        
