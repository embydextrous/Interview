from tree import Node

def find(root, a):
    if root is None:
        return False
    return root == a or find(root.left, a) or find(root.right, a)

def printCommonPath(root, a, b, path):
    if root is None:
        return None
    path.append(root.data)
    if root == a:
        if find(a, b):
            print(path)
        path.pop()
        return a
    if root == b:
        if find(b, a):
            print(path)
        path.pop()
        return b
    left = printCommonPath(root.left, a, b, path)
    right = printCommonPath(root.right, a, b, path)
    if left and right:
        print(path)
        return root
    path.pop()
    return left if left else right
    

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

printCommonPath(root, root.left, root.right.right.left, [])