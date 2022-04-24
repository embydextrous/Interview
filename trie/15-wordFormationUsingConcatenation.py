'''
Given a dictionary find out if given word can be made by two words in the dictionary. 
Note: Words in the dictionary must be unique and the word to be formed should not be a repetition of same 
words that are present in the Trie.

Examples: 

Input : dictionary[] = {"news", "abcd", "tree", "geeks", "paper"}   
        word = "newspaper"
Output : Yes
We can form "newspaper" using "news" and "paper"

Input : dictionary[] = {"geeks", "code", "xyz", 
                           "forgeeks", "paper"}   
        word = "geeksforgeeks"
Output : Yes

Input : dictionary[] = {"geek", "code", "xyz", 
                           "forgeeks", "paper"}   
        word = "geeksforgeeks"
Output : No
'''
from trie import Trie, charToIndex

def canMadeWord(words, target):
    trie = Trie(26)
    for word in words:
        trie.insert(word)
    p = trie.root
    for i in range(len(target)):
        index = charToIndex(target[i])
        if p.children[index] is None:
            return False
        p = p.children[index]
        if p.isEndOfWord:
            if trie.search(target[i+1:]):
                return True
    return False

words = ["geek", "code", "xyz", "forgeeks", "paper", "geeks"]
print(canMadeWord(words, "geeksforgeeks"))
