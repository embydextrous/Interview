from tree import Node

def preorder(root):
    if root is None:
        return
    s = [root]
    while len(s) > 0:
        node = s.pop()
        print(node.data, end=" ")
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
    print()

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

preorder(root)