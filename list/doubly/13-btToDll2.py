# https://www.geeksforgeeks.org/convert-a-binary-tree-into-doubly-linked-list-in-spiral-fashion/

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def btToDll(root):
    if root is None:
        return
    q1 = [root]
    q2 = []
    head = tail = Node('*')
    while len(q1) > 0 or len(q2) > 0:
        while len(q1) > 0:
            node = q1.pop()
            if node.right:
                q2.append(node.right)
            if node.left:
                q2.append(node.left)  
            tail.right = node
            node.left = tail
            tail = node
        print("q2: " + str([node.data for node in q2]))
        while len(q2) > 0:
            node = q2.pop()
            if node.left:
                q1.append(node.left)
            if node.right:
                q1.append(node.right)
            tail.right = node
            node.left = tail
            tail = node
        print("q1: " + str([node.data for node in q1]))
    head.right.left = None
    return head.right

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
root.right.left.right = Node(13)
root.right.right.left = Node(14)

s = btToDll(root)
print("head <-> ", end = "")
while s:
    print(s.data, end="")
    print(" <-> ", end="")
    s = s.right
print(" null")

