'''
Given an array of words, find all shortest unique prefixes to represent each word in the given array. 
Assume that no word is prefix of another. 
Examples: 
 

Input: arr[] = {"zebra", "dog", "duck", "dove"}
Output: dog, dov, du, z
Explanation: dog => dog
             dove => dov 
             duck => du
             zebra => z

Input: arr[] =  {"geeksgeeks", "geeksquiz", "geeksforgeeks"};
Output: geeksf, geeksg, geeksq}
'''
from trie import Trie, charToIndex

# Needs modification in TrieNode to store child count
def shortestUniquePrefix(words):
    trie = Trie(26)
    for word in words:
        trie.insert(word)
    for word in words:
        p = trie.root
        printed = False
        for i in range(len(word)):
            index = charToIndex(word[i])
            if p.children[index].childCount == 1 and not p.children[index].isEndOfWord:
                print(f"{word} -> {word[:i+1]}")
                printed = True
                break
            p = p.children[index]
        if not printed and p.isEndOfWord:
            print(f"{word} -> {word}")

words = ["zebra", "dog", "duck", "dove", "dogs", "doc", "doctor"]
shortestUniquePrefix(words)
        
        
            
