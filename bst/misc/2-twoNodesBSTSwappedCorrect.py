from bst import Node, inorder

def correctUtil(root, prevNode, a, b):
    if root:
        correctUtil(root.left, prevNode, a, b)
        if a[0] is None:
            if prevNode[0] is not None:
                if root.data < prevNode[0].data:
                    a[0] = prevNode[0]
        if prevNode[0] is not None and prevNode[0].data > root.data:
            b[0] = root
        prevNode[0] = root
        correctUtil(root.right, prevNode, a, b)

def correct(root):
    prevNode = [None]
    a = [None]
    b = [None]
    correctUtil(root, prevNode, a, b)
    a[0].data, b[0].data = b[0].data, a[0].data

'''
#      6
#     /   \
#   10    2
#  / \   / \
# 1   3 7   12
 
# Following 7 lines are for tree formation
'''
root = Node(6)
root.left = Node(10)
root.right = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(7)
root.right.right = Node(12)

inorder(root)
print()
correct(root)
inorder(root)
print()