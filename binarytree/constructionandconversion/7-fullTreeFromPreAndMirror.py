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
def construct(pre, preMirror):
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return Node(pre[0])
    data = pre[0]
    root = Node(data)
    a = pre[1]
    mirrorIndex = preMirror.index(a)
    root.left = construct(pre[1:len(pre) - mirrorIndex + 1], preMirror[mirrorIndex:])
    root.right = construct(pre[len(pre) - mirrorIndex + 1:], preMirror[1:mirrorIndex])
    return root

pre = [1, 2, 4, 5, 3, 6, 7]
preMirror = [1, 3, 7, 6, 2, 5, 4]
inorder(construct(pre, preMirror))
print()