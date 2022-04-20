'''
Given a string of length n of lowercase alphabet characters, we need to count total number of distinct 
substrings of this string.
Examples:

Input  : str = “ababa”
Output : 10
Total number of distinct substring are 10, which are,
"", "a", "b", "ab", "ba", "aba", "bab", "abab", "baba"
and "ababa"
'''
from trie import Trie

def countDistinctSubstrings(s):
    # Trie of all suffixes
    trie = Trie(26)
    for i in range(len(s)):
        trie.insert(s[i:])
    count = [0]
    countUtil(trie.root, count)
    return 1 + count[0]

def countUtil(node, count):
    for i in range(len(node.children)):
        if node.children[i] is not None:
            count[0] += 1
            countUtil(node.children[i], count)

s = "mississippi"
print(countDistinctSubstrings(s))

