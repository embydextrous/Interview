'''
Given a dictionary and a character array, print all valid words that are possible using characters
from the array. 
Examples: 
 
Input : Dict - {"go","bat","me","eat","goal", "boy", "run"} 
        arr[] = {'e','o','b', 'a','m','g', 'l'} 
Output : go, me, goal. 
'''
# At first looks we can simply use hash to solve this and this is not a use case for Trie.
# However, with Trie we can save for comparisons by comparing for a prefix only once.
# In example above we compare for go only once for go and goal saving us 2 comparisons.
from collections import Counter
from trie import Trie, indexToChar

def findWordUtil(root, chars, wordArray):
    if root.isEndOfWord:
        print("".join(wordArray))
    for i in range(len(root.children)):
        if root.children[i] is None:
            continue
        char = indexToChar(i)
        if char in chars:
            wordArray.append(char)
            findWordUtil(root.children[i], chars, wordArray)
            wordArray.pop()
    
def findWords(words, chars):
    chars = set(chars)
    trie = Trie(26)
    for word in words:
        trie.insert(word)
    p = trie.root
    findWordUtil(p, chars, [])

words = ["go","bat","me","eat","goal", "boy", "run"]
chars = ['e','o','b', 'a','m','g', 'l']
findWords(words, chars)
