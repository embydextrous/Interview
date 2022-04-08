class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def btToDll(root):
    # Base case
    head = tail = Node('*')
    btToDllInternal(root, [tail])
    return head.right

def btToDllInternal(root, tail):
    if root is None:
        return
    btToDllInternal(root.left, tail)
    tail[0].right = root
    root.left = tail[0]
    tail[0] = root
    btToDllInternal(root.right, tail)

a = Node(10)
a.left = Node(12)
a.right = Node(15)
a.left.left = Node(25)
a.left.right = Node(30)
a.right.left = Node(36)

s = btToDll(a)
while s:
    print(s.data, end=" ")
    s = s.right
print()


