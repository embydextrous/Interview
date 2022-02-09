from tree import Node, inorder

def convertToMirror(root):
    if root:
        root.left, root.right = root.right, root.left
        convertToMirror(root.left)
        convertToMirror(root.right)

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

convertToMirror(root)
inorder(root)
print()
