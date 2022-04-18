'''
Given a set of strings, find the longest common prefix.

Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
Output : "gee"

Input  : {"apple", "ape", "april"}
Output : "ap"
'''
from trie import Trie

def charToIndex(c):
    return ord(c) - ord('a')

def longestCommonPrefix(words):
    n = len(words)
    trie = Trie(26)
    for i in range(n - 1):
        trie.insert(words[i])
    lastWord = words[n-1]
    lastIndex = 0
    p = trie.root
    for c in lastWord:
        index = charToIndex(c)
        if p.children[index] is not None and p.children[index].count == n - 1:
            lastIndex += 1
            p = p.children[index]
        else:
            break
    return lastWord[:lastIndex]

a = ["apple", "ape", "april"]
print(longestCommonPrefix(a))




