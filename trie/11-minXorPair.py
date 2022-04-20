'''
Given an array of integers. Find the pair in an array that has a minimum XOR value. 
Examples : 
 

Input : arr[] =  {9, 5, 3}
Output : 6
        All pair with xor value (9 ^ 5) => 12, 
        (5 ^ 3) => 6, (9 ^ 3) => 10.
        Minimum XOR value is 6

Input : arr[] = {1, 2, 3, 4, 5}
Output : 1 
'''


# Keeping X fixed, XOR of X and Y decreases as Y approaches closer to X and becomes
# 0 when X == Y
# O(nlogn) Solution
def minXor(a):
    a.sort()
    mini = 10 ** 9
    for i in range(1, len(a)):
        mini = min(mini, a[i] ^ a[i-1]) 
    return mini

class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.value = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert MSB first
    def insert(self, n):
        p = self.root
        for i in range(31, -1, -1):
            index = (n >> i) & 1
            if p.children[index] is None:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.value = n

    # We first try to traverse to same bitm if not than to other bit
    # Because higher same set bit will yield higher power of 2 as 0
    def xorUtil(self, n):
        p = self.root
        for i in range(32, -1, -1):
            index = (n >> i) & 1
            if p.children[index] is not None:
                p = p.children[index]
            elif p.children[abs(index - 1)] is not None:
                p = p.children[abs(index - 1)]
        return p.value ^ n

# O(n) Solution - Actually 32 * O(n)
def minXor2(a):
    mini = 10 ** 9
    trie = Trie()
    trie.insert(a[0])
    for i in range(1, len(a)):
        mini = min(trie.xorUtil(a[i]), mini)
        trie.insert(a[i])
    return mini


a = [84, 87, 90]
print(minXor2(a))
for i in range(10, 100):
    print((i + 1) ^ 100)



# 01000100
# 00010010
# 00001100
# 01000010
# 00100000
# 00010101
# min - 7