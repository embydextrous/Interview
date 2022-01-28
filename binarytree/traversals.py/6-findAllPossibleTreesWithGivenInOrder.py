from tree import Node, preorder

def getTrees(arr , start , end):
    trees = []
    if start > end:
        trees.append(None)
        return trees
    for i in range(start, end + 1):
        lTrees = getTrees(arr, start, i - 1)
        rTrees = getTrees(arr, i + 1, end)
        for left in lTrees:
            for right in rTrees:
                node = Node(arr[i])
                node.left, node.right = left, right
                trees.append(node)
    return trees


ino = [4, 5, 7]
trees = getTrees(ino, 0, len(ino) - 1)
for root in trees:
    preorder(root)
    print()