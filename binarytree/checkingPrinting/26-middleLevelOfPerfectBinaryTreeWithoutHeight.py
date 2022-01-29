from tree import Node

def printMiddleLevelUtil(fast, slow):
    if fast is None or slow is None:
        return
    if fast.left is None and fast.right is None:
        print(slow.data, end = " ")
        return
    if fast.left.left:
        printMiddleLevelUtil(fast.left.left, slow.left)
        printMiddleLevelUtil(fast.left.left, slow.right)
    else:
        printMiddleLevelUtil(fast.left, slow.left)
        printMiddleLevelUtil(fast.left, slow.right)
    

def printMiddleLevel(root):
    if root is None:
        return
    printMiddleLevelUtil(root, root)

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.right = Node(10)
root.right.left = Node(7)
root.right.right = Node(14)

'''
        8
      /   \
     3     10
   /   \   /  \
  1    16 7   14
'''
printMiddleLevel(root)
print()
