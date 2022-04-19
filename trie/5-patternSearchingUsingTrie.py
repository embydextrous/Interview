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
from trie import Trie

class SuffixTrieNode:
    def __init__(self, alphabetSize):
        self.children = [None] * alphabetSize
        self.

    def __str__(self) -> str:
        return f"{self.children}"

class SuffixTrie:


def patternSearch(text, pattern):
    trie = Trie(256)
    N = len(text)
    # All suffixes trie
    for i in range(N):
        trie.insert(text[i:])
    p = trie.root
    for c in pattern:
        index = ord(c)
        if p.children[index] is None:
            return False
        p = p.children[index]
    return True

a = 

