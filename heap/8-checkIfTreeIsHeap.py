def checkIfHeap(root):
    if root is None:
        return
    q = [root]
    isFirstNonLeafNodeTraversed = False
    while len(q) > 0:
        node = q.pop(0)
        if isFirstNonLeafNodeTraversed:
            if node.left or node.right:
                return False
        else:
            if node.left and node.right:
                if node.left.data < node.data or node.right.data < node.data:
                    return False
                q.append(node.left)
                q.append(node.right)
            elif node.left:
                if node.left.data < node.data:
                    return False
                isFirstNonLeafNodeTraversed = True
                q.append(node.left)
            elif node.right:
                return False
            else:
                isFirstNonLeafNodeTraversed = True
    return True

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(checkIfHeap(root))

