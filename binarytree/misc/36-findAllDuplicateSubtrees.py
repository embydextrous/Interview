from tree import Node, inorder

def dupUtil(root, result, subtreesSet):
    if root is None:
        return ""
    left = dupUtil(root.left, result, subtreesSet)
    right = dupUtil(root.right, result, subtreesSet)
    subTreeKey = left + "|" + str(root.data) + "|" + right
    if subTreeKey in subtreesSet:
        if subtreesSet[subTreeKey] == 1:
            result.append(root)
    else:
        subtreesSet[subTreeKey] = 0
    subtreesSet[subTreeKey] += 1
    return subTreeKey

def duplicateSubTrees(root):
    result = []
    subtreesSet = {}
    dupUtil(root, result, subtreesSet)
    for tree in result:
        inorder(tree)
        print()

root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(2)
root.right.left.left = Node(4)
root.right.right = Node(4)
    
duplicateSubTrees(root)
