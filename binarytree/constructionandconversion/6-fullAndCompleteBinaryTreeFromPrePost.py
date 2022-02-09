from tree import Node, inorder

def construct(pre, post):
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return Node(pre[0])
    data = pre[0]
    root = Node(data)
    left = pre[1]
    postIndex = post.index(left)
    root.left = construct(pre[1:postIndex + 2], post[:postIndex+1])
    root.right = construct(pre[postIndex + 2:], post[postIndex+1 : len(post) - 1])
    return root

pre = [ 1, 2, 4, 8, 9, 5, 3, 6, 7 ]
post = [ 8, 9, 4, 5, 2, 6, 7, 3, 1 ]
size = len(pre)
inorder(construct(pre, post))
print()