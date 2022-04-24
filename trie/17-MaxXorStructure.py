'''
You are given a number of queries Q and each query will be of the following types:

    Query 1 : add(x) This means add x into your data structure.
    Query 2 : maxXOR(y) This means print the maximum possible XOR of y with all the elements already 
    stored in the data structure.

1 <= x, y <= 10^9 (1 Billion < 2 ^ 32)
1 <= 10^5 <= Q
The data structure begins with only a 0 in it.

Example:

Input: (1 10), (1 13), (2 10), (1 9), (1 5), (2 6)
Output: 7 15

Add 10 and 13 to stream.
Find maximum XOR with 10, which is 7
Insert 9 and 5
Find maximum XOR with 6 which is 15.


'''

class MaxXorNode:
    def __init__(self):
        self.children = [None] * 2

class MaxXorTrie:
    def __init__(self):
        self.root = MaxXorNode()

    def insert(self, n):
        p = self.root
        for i in range(31, -1, -1):
            index = (n >> i) & 1
            if p.children[index] is None:
                p.children[index] = MaxXorNode()
            p = p.children[index]

    def maxXor(self, x):
        p = self.root
        maxi = 0
        for i in range(31, -1, -1):
            index = (x >> i) & 1
            if p.children[abs(index - 1)]:
                maxi <<= 1
                maxi = maxi | 1
                p = p.children[abs(index - 1)]
            else:
                maxi <<= 1
                p = p.children[index]
        return maxi

maxXorTrie = MaxXorTrie()
maxXorTrie.insert(10)
maxXorTrie.insert(13)
print(maxXorTrie.maxXor(10))
maxXorTrie.insert(9)
maxXorTrie.insert(5)
print(maxXorTrie.maxXor(6))
'''
    1010 1101
         1
     0       1
      1     0
     0        1
'''


