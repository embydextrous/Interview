# https://www.geeksforgeeks.org/convert-an-arbitrary-binary-tree-to-a-tree-that-holds-children-sum-property/

from tree import Node, inorder

'''
              50
           /     \     
          /       \
         7         2
        / \       / \
     /     \     /   \
    3        5  1     30
'''

def convert(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    left = convert(root.left)
    right = convert(root.right)
    diff = left + right - root.data
    if diff >= 0:
        root.data += diff
    else:
        if root.left:
            increment(root.left, diff * -1)
        elif root.right:
            increment(root.right, diff * -1)
    return root.data

def increment(root, diff):
    root.data += diff
    print(diff)
    if root.left:
        increment(root.left, diff)
    elif root.right:
        increment(root.right, diff)

root = Node(50)
root.left = Node(7)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(30)

convert(root)
inorder(root)
print()



    
