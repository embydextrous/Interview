from tree import Node, inorder
# https://www.geeksforgeeks.org/given-a-binary-tree-how-do-you-remove-all-the-half-nodes/

def removeHalfNodes(root):
    if root is None:
        return
    removeHalfNodes(root.left)
    removeHalfNodes(root.right)
    if root.left and root.right is None:
        root.data = root.left.data
        root.left = None
    elif root.right and root.left is None:
        root.data = root.right.data
        root.right = None

'''
                1
             /     \  
          (2)       3
          /       /   \ 
        (4)      5     6
          \     / \
           7   8   9
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.left.left.right = Node(7)
root.right.left.left = Node(8)
root.right.left.right = Node(9)

removeHalfNodes(root)
inorder(root)
print()



