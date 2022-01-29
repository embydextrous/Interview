from tree import Node

def printRightView(root):
    if root is None:
        return
    q1, q2 = [root], []
    while len(q1) > 0:
        while len(q1) > 0:
            node = q1.pop(0)
            if len(q1) == 0:
                print(node.data, end = " ")
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        q1, q2 = q2, q1
    print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

printRightView(root)