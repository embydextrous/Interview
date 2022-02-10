from bst import Node, insert, search

# Assuming a and b are in BST
def lca(root, a, b):
    if root is None:
        return None
    if root.data >= a and root.data <= b or root.data >= b and root.data <= a:
        return root if search(root, a) and search(root, b) else None
    if root.data > a and root.data > b:
        return lca(root.left, a, b)
    return lca(root.right, a, b)

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
print(lca(root, 7, 12).data)
