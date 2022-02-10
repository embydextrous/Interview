from bst import Node, insert

# Morris Traversal, Also see, https://www.geeksforgeeks.org/kth-largest-element-bst-using-constant-extra-space/

def kthSmallest(root, k):
    while root:
        if root.left:
            rightMost = root.left
            while rightMost.right and rightMost.right != root:
                rightMost = rightMost.right
            if rightMost.right == root:
                k -= 1
                if k == 0:
                    return root.data
                rightMost.right = None
                root = root.right
            else:
                rightMost.right = root
                root = root.left
        else:
            k -= 1
            if k == 0:
                return root.data
            root = root.right

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

print(kthSmallest(root, 7))
