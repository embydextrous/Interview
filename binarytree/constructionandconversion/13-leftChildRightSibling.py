class Node:
    def __init__(self, data):
        self.data = data
        self.child = None
        self.next = None

def addSibling(node, data):
    if node == None:
        return None
    while node.next:
        node = node.next
    node.next = Node(data)
    return node.next

def addChild(node, data):
    if node == None:
        return
    if node.child:
        return addSibling(node.child, data)
    else:
        node.child = Node(data)
        return node.child

def traverse(root):
    if root:
        print(root.data, end = " ")
        traverse(root.child)
        traverse(root.next)

root = Node(10)
n1 = addChild(root, 2)
n2 = addChild(root, 3)
n3 = addChild(root, 4)
n4 = addChild(n3, 6)
n5 = addChild(root, 5)
n6 = addChild(n5, 7)
n7 = addChild(n5, 8)
n8 = addChild(n5, 9)
traverse(root)
print()