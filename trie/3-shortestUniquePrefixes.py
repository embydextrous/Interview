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
from trie import Trie

def charToIndex(c):
    return ord(c) - ord('a')

def shortestUniquePrefix(words):
    trie = Trie(26)
    for word in words:
        trie.insert(word)
    for word in words:
        prefix = []
        p = trie.root
        for c in word:
            index = charToIndex(c)
            prefix.append(c)
            p = p.children[index]
            if p.setChildCount == 1 and not p.isEndOfWord:
                break
        print ("{} -> {}".format(word, "".join(prefix)))


a = ["zebra", "dog", "duck", "dove", "dogs"]
shortestUniquePrefix(a)