from tree import Node, inorder

def construct(pre, preLeft, preRight, post, postLeft, postRight):
    if preLeft > preRight:
        return None
    if preLeft == preRight:
        return Node(pre[preLeft])
    root = Node(pre[preLeft])
    left = pre[preLeft + 1]
    postIndex = post.index(left)
    root.left = construct(pre, preLeft + 1, preLeft + postIndex - postLeft + 1, post, postLeft, postIndex)
    root.right = construct(pre, preLeft + postIndex - postLeft + 2, preRight, post, postIndex + 1, postRight - 1)
    return root

'''
            1
          /   \
         2     3
        / \   /  \
       4   5 6    7
      / \
     8   9     
'''
pre = [ 1, 2, 4, 8, 9, 5, 3, 6, 7 ]
post = [ 8, 9, 4, 5, 2, 6, 7, 3, 1 ]
size = len(pre)
inorder(construct(pre, 0, len(pre) - 1, post, 0, len(post) - 1))
print()