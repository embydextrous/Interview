from tree import Node, preorder

def construct(post, ino, postIndex, inoLeft, inoRight):
    if postIndex[0] < 0 or inoLeft > inoRight:
        return None
    root = Node(post[postIndex[0]])
    inoIndex = ino.index(root.data, inoLeft, inoRight + 1)
    postIndex[0] -= 1
    root.right = construct(post, ino, postIndex, inoIndex + 1, inoRight)
    root.left = construct(post, ino, postIndex, inoLeft, inoIndex - 1)
    return root

inOrder = [4, 8, 2, 5, 1, 6, 3, 7]
postOrder = [8, 4, 5, 2, 6, 7, 3, 1]

'''
          1
       /     \
     2        3
   /    \   /   \
  4     5   6    7
    \
      8 
'''
n = len(inOrder)
preorder(construct(postOrder, inOrder, [n-1], 0, len(inOrder) - 1))
print()