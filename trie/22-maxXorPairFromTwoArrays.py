'''
Two arrays A and B consisting of N elements are given. The task is to compute the maximum possible 
XOR of every element in array A with array B.

Examples:  

Input :
A : 7 3 9 12
B : 1 3 5 2
Output : 6 6 12 15
Explanation : 
1 xor 12 = 13
3 xor 12 = 15
5 xor 9 = 12
2 xor 12 = 14
'''
from binarytrie import BinaryTrie

def maxXorPair(a, b):
    binaryTrie = BinaryTrie()
    for x in a:
        binaryTrie.insert(x)
    for x in b:
        maxXor = binaryTrie.maxXor(x)
        print(f"{maxXor ^ x} ^ {x} = {maxXor}")

a = [7, 3, 9, 12]
b = [1, 3, 5, 2]
maxXorPair(a, b)