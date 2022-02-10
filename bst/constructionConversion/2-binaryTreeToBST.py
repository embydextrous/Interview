from bst import Node, inorder

def preorder(root, a):
    if root:
        a.append(root.data)
        preorder(root.left, a)
        preorder(root.right, a)

def btToBstUtil(root, a, idx):
    if root:
        btToBstUtil(root.left, a, idx)
        root.data = a[idx[0]]
        idx[0] += 1
        btToBstUtil(root.right, a, idx)

def btToBst(root):
    if root is None:
        return
    a = []
    preorder(root, a)
    a.sort()
    idx = [0]
    btToBstUtil(root, a, idx)

root = Node(10)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(8)
root.left.right = Node(4)

btToBst(root)
inorder(root)
print()
