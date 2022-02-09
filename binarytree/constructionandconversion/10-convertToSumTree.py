from tree import Node, inorder

def convertSum(root):
    if root is None:
        return 0
    left = convertSum(root.left)
    right = convertSum(root.right)
    retValue = root.data + left + right
    root.data = left + right
    return retValue

'''
         8
       /   \  
      3     11
     / \    / \
    -1 1   3   7
'''

root = Node(8)
root.left = Node(3)
root.right = Node(11)
root.left.left = Node(-1)
root.left.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(7)

convertSum(root)
inorder(root)
print()