'''
Given an array arr[] of strings, the task is to print the strings from the array which are not prefix of any 
other string from the same array.
Examples: 
    Input: arr[] = {“apple”, “app”, “there”, “the”, “like”} 
    Output: 
    apple 
    like 
    there 
    Here “app” is a prefix of “apple” 
    Hence, it is not printed and 
    “the” is a prefix of “there”
    Input: arr[] = {“a”, “aa”, “aaa”, “aaaa”} 
    Output: 
    aaaa 
'''
# Also see, https://www.geeksforgeeks.org/count-the-number-of-words-with-given-prefix-using-trie/
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

def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    print(trie.root.children[0].children)
    for word in words:
        p = trie.root
        for c in word:
            index = charToIndex(c)
            p = p.children[index]
        if p.count == 1:
            print(word)

words = ["apple", "app", "there", "the", "like"]
solution(words)