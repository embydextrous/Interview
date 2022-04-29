from tree import Node

def inorder(root, ino):
    if root:
        inorder(root.left, ino)
        ino.append(root.data)
        inorder(root.right, ino)

def minSwaps(root):
    a = []
    inorder(root, a)
    arrPos = [[a[i], i] for i in range(len(a))]
    arrPos.sort(key = lambda x : x[0])
    print(arrPos)
    visited = set()
    result = 0
    i = 0
    while i < len(a):
        cycleLength = 0
        while i not in visited:
            visited.add(i)
            i = arrPos[i][1]
            cycleLength += 1
        result += max(0, cycleLength - 1)
        i += 1
    return result

'''
            8
          /   \ 
         3     1
       /      /
      2      6
       \    / \
        4  5   7   
'''
# 2 4 3 8 5 6 7 1

root = Node(8)
root.left = Node(3)
root.right = Node(1)
root.left.left = Node(2)
root.right.left = Node(6)
root.right.left.left = Node(5)
root.right.left.right = Node(7)
root.left.left.right = Node(4)
print(minSwaps(root))