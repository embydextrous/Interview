# https://www.geeksforgeeks.org/find-sum-nodes-given-perfect-binary-tree/

def findSum(levels):
    numLeafs = 2 ** (levels - 1)
    return (levels * (numLeafs + 1) * numLeafs) // 2

print(findSum(4))
