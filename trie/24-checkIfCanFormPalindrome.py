'''
Given a list of words, find if any of the two words can be joined to form a palindrome.
Examples: 

Input  : list[] = {"geekf", "geeks", "or", 
                            "keeg", "abc", "bc"}
Output : Yes
There is a pair "geekf" and "keeg"

Input : list[] =  {"abc", "xyxcba", "geekst", "or",
                                      "keeg", "bc"}
Output : Yes
There is a pair "abc" and "xyxcba"
'''
from trie import charToIndex

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.id = -1

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.words = words
        for i in range(len(words)):
            self.insertReverse(words[i], i)

    def isPalindrome(self, word, start, end):
        while start != end:
            if word[start] == word[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def insertReverse(self, word, id):
        p = self.root
        for i in range(len(word) - 1, -1, -1):
            index = charToIndex(word[i])
            if p.children[index] is None:
                p.children[index] = TrieNode()
            if (self.isPalindrome(word, 0, i - 1)):
                p.children[index].id = id
            p = p.children[index]
        p.id = id
        p.isEndOfWord = True

    def canFormPalindrome(self, word):
        p = self.root
        for i in range(len(word)):
            index = charToIndex(word[i])
            if p.children[index] is None:
                print(f"{word}{self.words[p.id]}")
                return self.isPalindrome(word, i, len(word) - 1)
            p = p.children[index]
        if p.id != -1:
            print(f"{word}{self.words[p.id]}")
            return True

words = ["abc", "xyxcba", "geekst", "or", "keeg", "bc"]
trie = Trie(words)
canFormPalindrome = False
trie.canFormPalindrome("abc")