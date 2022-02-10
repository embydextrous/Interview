from bst import Node, insert

def findSmallest(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.data

def findLargest(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.data

'''
            7
          /   \
         3     12
        / \    /
       1   5  8
          /    \
         4      11
'''

root = Node(7)
insert(root, 3)
insert(root, 12)
insert(root, 5)
insert(root, 1)
insert(root, 4)
insert(root, 8)
insert(root, 11)

print(findSmallest(root))
print(findLargest(root))