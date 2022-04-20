'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints
all occurrences of pat[] in txt[]. You may assume that n > m.

As discussed in the previous post, we discussed that there are two ways efficiently solve the above problem.
1) Preprocess Pattern: KMP Algorithm, Rabin Karp Algorithm, Finite Automata, Boyer Moore Algorithm.
2) Preprocess Text: Suffix Tree

The best possible time complexity achieved by first (preprocessing pattern) is O(n) and by second 
(preprocessing text) is O(m) where m and n are lengths of pattern and text respectively.

Note that the second way does the searching only in O(m) time and it is preferred when text doesn't change 
very frequently and there are many search queries. We have discussed Suffix Tree (A compressed Trie of all 
suffixes of Text) .
Implementation of Suffix Tree may be time consuming for problems to be coded in a technical interview or 
programming contexts. The implementation is close to suffix tree, the only thing is, it's a simple Trie 
instead of compressed Trie.

As discussed in Suffix Tree post, the idea is, every pattern that is present in text (or we can say every 
substring of text) must be a prefix of one of all possible suffixes. So if we build a Trie of all suffixes, 
we can find the pattern in O(m) time where m is pattern length.

Building a Trie of Suffixes 
1) Generate all suffixes of given text. 
2) Consider all suffixes as individual words and build a trie.
'''
from trie import charToIndex

class SuffixTrieNode:
    def __init__(self, alphabetSize):
        self.children = [None] * alphabetSize
        self.indexes = []

    def __str__(self) -> str:
        return f"{self.children}"

class SuffixTrie:
    def __init__(self, alphabetSize, text):
        self.alphabetSize = alphabetSize
        self.root = SuffixTrieNode(alphabetSize)
        for i in range(len(text)):
            self.insertSuffix(text, i)

    def insertSuffix(self, text, startIndex):
        n = len(text)
        p = self.root
        for i in range(startIndex, n):
            index = charToIndex(text[i])
            if p.children[index] is None:
                p.children[index] = SuffixTrieNode(self.alphabetSize)
            p.children[index].indexes.append(i)
            p = p.children[index]

    def search(self, pattern):
        p = self.root
        for c in pattern:
            index = charToIndex(c)
            if p.children[index] is None:
                return []
            p = p.children[index]
        return [i - len(pattern) + 1 for i in p.indexes]

def patternSearch(text, pattern):
    suffixTrie = SuffixTrie(26, text)
    indexes = suffixTrie.search(pattern)
    if len(indexes) == 0:
        print(f"{pattern} not found")
    for i in indexes:
        print(f"{pattern} found at {i}")
    

a = "geeksforgeeksdotorg"
patternSearch(a, "geek")
patternSearch(a, "e")
patternSearch(a, "quiz")
patternSearch(a, "for")



