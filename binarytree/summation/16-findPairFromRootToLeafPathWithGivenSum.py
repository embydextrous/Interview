from tree import Node

def findPairUtil(root, rootSet, x, pair):
    if x - root.data in rootSet:
        pair[0], pair[1] = x - root.data, root.data
        return
    if root.data in rootSet:
        rootSet[root.data] += 1
    else:
        rootSet[root.data] = 1
    if root.left:
        findPairUtil(root.left, rootSet, x, pair)
    if root.right:
        findPairUtil(root.right, rootSet, x, pair)
    if rootSet[root.data] == 1:
        rootSet.pop(root.data)
    else:
        rootSet[root.data] -= 1

def findPair(root, x):
    if root is None:
        return
    pair = [-1, -1]
    findPairUtil(root, {}, x, pair)
    return pair

def hasPair(root, s, x):
    if root is None:
        return False
    if x - root.data in s:
        return True
    s.add(root.data)
    res = hasPair(root.left, s, x) or hasPair(root.right, s, x)
    s.remove(root.data)
    return res

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)
print(findPair(root, 15))
print(hasPair(root, set(), 10))


