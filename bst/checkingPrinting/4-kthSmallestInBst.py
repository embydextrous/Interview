from bst import Node, insert

# https://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/ - Simply do reverse inorder traversal
# Also see, https://www.geeksforgeeks.org/second-largest-element-in-binary-search-tree-bst/

def kthSmallest(root, k):
    if root:
        kthSmallest(root.left, k)
        k[0] -= 1
        if k[0] == 0:
            print(root.data)
        kthSmallest(root.right, k)

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

kthSmallest(root, [8])
