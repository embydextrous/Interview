from bst import Node, preorder

def getTreesUtil(start, end):
    trees = []
    if start > end:
        trees.append(None)
        return trees
    for i in range(start, end + 1):
        lTrees = getTreesUtil(start, i - 1)
        rTrees = getTreesUtil(i + 1, end)
        for left in lTrees:
            for right in rTrees:
                node = Node(i)
                node.left = left
                node.right = right
                trees.append(node)
    return trees

def getTrees(N):
    return getTreesUtil(1, N)

'''
    1          1          2          3           3
     \          \        / \        /           /
      2          3      1   3      1           2
       \        /                   \         /
        3      2                     2       1
'''

N = 3
trees = getTrees(N)
for tree in trees:
    preorder(tree)
    print()


