'''
Given an array of strings arr[] and Q queries where each each query consists of a string str, 
the task is to find the longest string in the array that matches with prefix of the given string str 
i.e. the string must be prefix of str.

Examples:

    Input: arr[] = {"GeeksForGeeks", "GeeksForGeeksd", "Arnab", "Art"},
    q[] = {"GeeksForGeeks", "Ar", "Art"}
    Output:
    GeeksForGeeks
    Arnab
    Art

    Input: arr[] = {"Geek", "Geek", "Geekss", "Geekk"},
    q[] = {"Geek", "Geeks", "Geekk", "Gee"}
    Output:
    Geekss
    Geekss
    Geekk
    Geekss
'''
class TrieNode:
    def __init__(self):
        self.children = [None] * 256
        self.isEndOfWord = False
        self.longestWord = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        if len(p.longestWord) < len(word):
            p.longestWord = word
        for c in word:
            index = ord(c)
            if p.children[index] is None:
                p.children[index] = TrieNode()
            p = p.children[index]
            if len(p.longestWord) < len(word):
                p.longestWord = word
        p.isEndOfWord = True

    def findLongestWordForPrefix(self, prefix):
        p = self.root
        for c in prefix:
            index = ord(c)
            if p.children[index] is None:
                return -1
            p = p.children[index]
        return p.longestWord

def printLongestWord(words, prefixes):
    trie = Trie()
    for word in words:
        trie.insert(word)
    for prefix in prefixes:
        print(f"Longest word for {prefix} is {trie.findLongestWordForPrefix(prefix)}")

words = ["GeeksForGeeks", "GeeksForGeeksd", "Arnab", "Art"]
prefixes = ["GeeksForGeeks", "Ar", "Art"]

printLongestWord(words, prefixes)