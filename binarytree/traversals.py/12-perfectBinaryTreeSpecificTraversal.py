# https://www.geeksforgeeks.org/perfect-binary-tree-specific-level-order-traversal/
from tree import Node

def perfectBinaryTreeSpecificLevelOrderTraversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    if root.left is None:
        return
    q = [root.left, root.right]
    while len(q) > 0:
        a, b = q.pop(0), q.pop(0)
        print(a.data, end= " ")
        print(b.data, end= " ")
        if a.left:
            q.append(a.left)
        if b.right:
            q.append(b.right)
        if a.right:
            q.append(a.right)
        if b.left:
            q.append(b.left)
    print()

def perfectSpecificTraversal(root):
    if root is None:
        return
    print(root.data, end = " ")
    if root.left is None:
        print()
        return
    q = [root.left, root.right]
    while len(q) > 0:
        node1, node2 = q.pop(0), q.pop(0)
        print(node1.data, end = " ")
        print(node2.data, end = " ")
        if node1.left:
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)
    print()



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)

root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
perfectSpecificTraversal(root)