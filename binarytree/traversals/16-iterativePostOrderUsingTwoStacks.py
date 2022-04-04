from tree import Node

def postorder(root):
    if root is None:
        return
    s1 = [root]
    s2 = []
    while len(s1) > 0:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while len(s2) > 0:
        print(s2.pop().data, end = " ")
    print()

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

postorder(root)