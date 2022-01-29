from tree import Node

def printLevelOfEachNode(root, level):
    if root:
        printLevelOfEachNode(root.left, level + 1)
        print(str(root.data) + " -> ", str(level))
        printLevelOfEachNode(root.right, level + 1)

root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(4)
printLevelOfEachNode(root, 1)