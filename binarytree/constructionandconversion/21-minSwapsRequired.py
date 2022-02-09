from tree import Node

def inorder(root, ino):
    if root:
        inorder(root.left, ino)
        ino.append(root.data)
        inorder(root.right, ino)

def minSwaps(root):
    a = []
    inorder(root, a)
    if len(a) < 2:
        return 0
    sortedA = sorted(a)
    swaps = 0
    indexHash = {a[i]:i for i in range(len(a))}
    for i in range(len(a)):
        print(a)
        if a[i] != sortedA[i]:
            swaps += 1
            indexInA = indexHash[sortedA[i]]
            a[i], a[indexInA] = a[indexInA], a[i] 
            indexHash[sortedA[i]] = i
            indexHash[a[indexInA]] = indexInA   
        print(a)
    return swaps

'''
            7
          /   \ 
         8     1
       /      /
      4      3
       \    / \
        5  6   2   
'''

root = Node(7)
root.left = Node(8)
root.right = Node(1)
root.left.left = Node(4)
root.right.left = Node(3)
root.right.left.left = Node(6)
root.right.left.right = Node(2)
root.left.left.right = Node(5)
print(minSwaps(root))