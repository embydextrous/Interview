from tree import Node

def btToDll(root, prevNode, result):
    if root:
        btToDll(root.left, prevNode, result)
        if result[0] is None:
            result[0] = root
        root.left = prevNode[0]
        if prevNode[0]:
            prevNode[0].right = root
        prevNode[0] = root
        btToDll(root.right, prevNode, result)

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

result = [None]
btToDll(root, [None], result)
root = result[0]
while root:
    print(root.data, end = " ")
    root = root.right
print()
