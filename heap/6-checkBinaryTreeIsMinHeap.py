class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkIfMaxHeap(root):
    if root is None:
        return True
    q = [root]
    isFirstIncompleteNodeGone = False
    while len(q) > 0:
        node = q.pop(0)
        if isFirstIncompleteNodeGone:
            if node.left or node.right:
                return False
        else:
            if node.left and node.right:
                if node.left.data > node.data:
                    return False
                else:
                    q.append(node.left)
                if node.right.data > node.data:
                    return False
                else:
                    q.append(node.right)
            elif node.left:
                isFirstIncompleteNodeGone = True
                if node.left.data > node.data:
                    return False
                else:
                    q.append(node.left)
            elif node.right:
                return False
    return True

root = Node(10)
root.left = Node(9)
root.right = Node(8)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
root.left.left.left = Node(3)
root.left.left.right = Node(2)
root.left.right.left = Node(1)

print(checkIfMaxHeap(root))



        