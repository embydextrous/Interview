from tree import Node

def btToDllSpiral(root):
    if root is None:
        return
    s1, s2 = [root], []
    prevNode = None
    while len(s1) > 0 or len(s2) > 0:
        while len(s1) > 0:
            node = s1.pop()
            if node.right:
                s2.append(node.right)
            if node.left:
                s2.append(node.left)
            node.left = prevNode
            if prevNode:
                prevNode.right = node
            prevNode = node
        while len(s2) > 0:
            node = s2.pop()
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
            node.left = prevNode
            if prevNode:
                prevNode.right = node
            prevNode = node
    return root

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

root = btToDllSpiral(root)

while root:
    print(root.data, end = " ")
    root = root.right
print()