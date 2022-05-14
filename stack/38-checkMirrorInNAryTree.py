from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.child = []

def checkMirror(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    q1, q2 = deque([deque([a])]), deque([deque([b])])
    while len(q1) > 0 and len(q2) > 0:
        n1, n2 = q1.popleft(), q2.popleft()
        if len(n1) != len(n2):
            return False
        while len(n1) > 0 and len(n2) > 0:
            x, y = n1.popleft(), n2.pop()
            if x.data != y.data:
                return False
            q1.append(deque(x.child))
            q2.append(deque(y.child))
    return True

root1 = Node(1)
root1.child = [Node(2), Node(3), Node(4), Node(5)]
root1.child[0].child = [Node(6), Node(7)]
root1.child[1].child = [Node(8)]
root1.child[3].child = [Node(9), Node(10), Node(11)]

root2 = Node(1)
root2.child = [Node(5), Node(4), Node(3), Node(2)]
root2.child[3].child = [Node(7), Node(6)]
root2.child[2].child = [Node(8)]
root2.child[0].child = [Node(11), Node(10), Node(9)]

print(checkMirror(root1, root2))