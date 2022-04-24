class BinaryTrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.data = None

class BinaryTrie:
    def __init__(self):
        self.root = BinaryTrieNode()

    def insert(self, n):
        p = self.root
        for i in range(31, -1, -1):
            index = (n >> i) & 1
            if p.children[index] is None:
                p.children[index] = BinaryTrieNode()
            p = p.children[index]
        p.data = n
    
    def maxXor(self, x):
        p = self.root
        maxi = 0
        for i in range(31, -1, -1):
            index = (x >> i) & 1
            if p.children[abs(index - 1)]:
                maxi <<= 1
                maxi |= 1
                p = p.children[abs(index - 1)]
            else:
                maxi <<= 1
                p = p.children[index]
        return maxi

    def minXor(self, x):
        p = self.root
        mini = 0
        for i in range(31, -1, -1):
            index = (x >> i) & 1
            if p.children[index]:
                mini <<= 1
                p = p.children[index]
            else:
                mini <<= 1
                mini |= 1
                p = p.children[abs(index - 1)]
        return mini
