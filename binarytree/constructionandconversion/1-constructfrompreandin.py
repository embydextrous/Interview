from tree import Node, postorder

# Can construct tree
# pre in - yes
# post in - yes
# level in - yes
# pre post - no
# pre level - no
# post level - no
def construct(pre, ino, preIndex, inoLeft, inoRight):
    if preIndex[0] >= len(pre) or inoLeft > inoRight:
        return None
    root = Node(pre[preIndex[0]])
    inoIndex = ino.index(root.data, inoLeft, inoRight + 1)
    preIndex[0] += 1
    root.left = construct(pre, ino, preIndex, inoLeft, inoIndex - 1)
    root.right = construct(pre, ino, preIndex, inoIndex + 1, inoRight)
    return root

inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

'''
            A
         /     \
        B       C
       / \     /
      D   E   F     
'''

postorder(construct(preOrder, inOrder, [0], 0, len(inOrder) - 1))
print()