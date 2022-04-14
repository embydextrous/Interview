class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bt2dll(root):
    head = tail = Node('*')
    bt2dllInternal(root, tail)
    if head.right is None:
        return None
    right = head.right
    right.left = None
    head.right = None
    return right

def bt2dllInternal(root, tail):
    if root is None:
        return
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        left, right = node.left, node.right
        tail.right = node
        node.left = tail
        tail = tail.right
        if left:
            q.append(left)
        if right:
            q.append(right)


a = Node(10)
a.left = Node(12)
a.right = Node(15)
a.left.left = Node(25)
a.left.right = Node(30)
a.right.left = Node(36)

s = bt2dll(a)
while s:
    print(s.data, end=" ")
    s = s.right
print()


