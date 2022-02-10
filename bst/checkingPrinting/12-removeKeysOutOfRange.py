from bst import Node, inorder, insert

def removeKeys(root, k1, k2):
    if root is None:
        return None
    if root.data >= k1 and root.data <= k2:
        root.left = removeKeys(root.left, k1, k2)
        root.right = removeKeys(root.right, k1, k2)
        return root
    if root.data < k1:
        root.right = removeKeys(root.right, k1, k2)
        return root.right
    if root.data > k2:
        root.left = removeKeys(root.left, k1, k2)
        return root.left
'''
            12
          /    \
         7     21
       /  \    / \
      2    8  16  24
       \    \   \
        6    11  18   
'''
root = Node(12)
insert(root, 7)
insert(root, 8)
insert(root, 11)
insert(root, 2)
insert(root, 6)
insert(root, 21)
insert(root, 16)
insert(root, 18)
insert(root, 24)

inorder(root)
print()
root = removeKeys(root, 9, 22)
inorder(root)
print()
