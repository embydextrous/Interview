from tree import Node

# Also see this, https://www.geeksforgeeks.org/find-next-right-node-given-key-set-2/

def connectNodesAtSameLevel(root):
    if root is None:
        return
    q1, q2 = [root], []
    while len(q1) > 0:
        lastNode = None
        while len(q1) > 0:
            node = q1.pop(0)
            if lastNode:
                lastNode.next = node
            lastNode = node
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        q1, q2 = q2, q1
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
connectNodesAtSameLevel(root)
current = root
while current:
    print(current.data, end = " ")
    current = current.next
print()

current = root.left
while current:
    print(current.data, end = " ")
    current = current.next
print()

current = root.left.left
while current:
    print(current.data, end = " ")
    current = current.next
print()