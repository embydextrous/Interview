'''
Given a dictionary of words and an input string, find the longest prefix of the string which is also 
a word in dictionary.

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
from trie import Trie

class Solution:
    def __init__(self, words):
        self.trie = Trie(26)
        for word in words:
            self.trie.insert(word)

    def charToIndex(self, c):
        return ord(c) - ord('a')

    def getLongestPrefix(self, key):
        pCrawl = self.trie.root
        result = []
        segment = []
        for c in key:
            index = self.charToIndex(c)
            if pCrawl.children[index]:
                segment.append(c)
                if pCrawl.children[index].isEndOfWord:
                    result.append("".join(segment))
                    segment.clear()
                pCrawl = pCrawl.children[index]
            else:
                return "".join(result)
        return "".join(result)

words = ["are", "area", "base", "cat", "cater", "children", "basement"]
s = Solution(words)
print(s.getLongestPrefix("caterer"))
print(s.getLongestPrefix("basemexy"))
print(s.getLongestPrefix("child"))



