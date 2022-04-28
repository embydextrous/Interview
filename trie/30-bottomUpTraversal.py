'''
Input :
                                          root
                                         /    \    
                                         a     t     
                                         |     |     
                                         n     h     
                                         | \   |   
                                         s  y  e     
                                         |     |  \ 
                                         w     i   r
                                         |     |   |
                                         e     r   e
                                         |        
                                         r        
Output : r, e, w, s, y, n, a, r, i, e, r, e, h, t  

Input : 
                                           root
                                          /     \    
                                         c       t     
                                         |       |     
                                         a       h     
                                         | \     |     
                                         l  t    e     
                                         |       |  \ 
                                         l       i   r
                                         | \     |   |
                                         e  i    r   e
                                         |  |
                                         r  n
                                            |
                                            g 

Output : r, e, g, n, i, l, l, t, a, c, r, i, e, r, e, h, t
'''
from trie import Trie, indexToChar

def bottomUpTraversal(root, char):
    if root is None:
        return
    for i in range(len(root.children)):
        if root.children[i] is not None:
            c = indexToChar(i)
            bottomUpTraversal(root.children[i], c)
    if char is not None:
        print(char, end = " ")

words = ["caller", "calling", "cat", "their", "there"]
trie = Trie(26)
for word in words:
    trie.insert(word)
bottomUpTraversal(trie.root, None)
print()

    