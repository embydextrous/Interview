# https://www.geeksforgeeks.org/construct-full-binary-tree-using-preorder-traversal-preorder-traversal-mirror-tree/

from tree import Node, inorder

'''
Input :  preOrder[] = {1,2,4,5,3,6,7}
         preOrderMirror[] = {1,3,7,6,2,5,4}

Output :          1
               /    \
              2      3
            /   \   /  \
           4     5 6    7
'''
def construct(pre, preLeft, preRight, mirror, mirrorLeft, mirrorRight):
    if preLeft > preRight:
        return None
    if preLeft == preRight:
        return Node(pre[preLeft])
    root = Node(pre[preLeft])
    left = pre[preLeft + 1]
    mirrorIndex = mirror.index(left)
    root.left = construct(pre, preLeft + 1, preLeft + mirrorIndex - mirrorLeft - 1, mirror, mirrorIndex, mirrorRight)
    root.right = construct(pre, preLeft + mirrorIndex - mirrorLeft, preRight, mirror, mirrorLeft + 1, mirrorIndex - 1)
    return root

pre = [1, 2, 4, 5, 3, 6, 7]
mirror = [1, 3, 7, 6, 2, 5, 4]
n = len(mirror)
inorder(construct(pre, 0, n - 1, mirror, 0, n - 1))
print()