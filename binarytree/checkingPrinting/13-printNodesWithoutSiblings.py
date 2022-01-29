from tree import Node

def printNodesWithoutSiblings(root):
    if root is None:
        return
    q = [(root, False)]
    while len(q) > 0:
        (node, shouldPrintSibling) = q.pop(0)
        if shouldPrintSibling:
            print(node.data, end = " ")
        if node.left:
            q.append((node.left, not node.right))
        if node.right:
            q.append((node.right, not node.left))
    print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.left.left = Node(6)

printNodesWithoutSiblings(root)