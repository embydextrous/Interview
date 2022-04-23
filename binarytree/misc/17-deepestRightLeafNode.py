from tree import Node
from collections import deque

# Also see, https://www.geeksforgeeks.org/deepest-left-leaf-node-in-a-binary-tree/
# Also see, https://www.geeksforgeeks.org/find-deepest-node-binary-tree/

def deepestRightNode(root):
    if root is None:
        return True
    q = deque([(root, True)])
    result = None
    while len(q) > 0:
        node, isRightNode = q.popleft()
        if isRightNode and node.left is None and node.right is None:
            result = node
        if node.left:
            q.append((node.left, False))
        if node.right:
            q.append((node.right, True))
    return result
    
def deepestRightNodeUtil(root, lvl, maxLevel, isRight, result):
    if root:
        if lvl > maxLevel[0] and isRight and root.left is None and root.right is None:
            maxLevel[0] = lvl
            result[0] = root
        deepestRightNodeUtil(root.left, lvl + 1, maxLevel, False, result)
        deepestRightNodeUtil(root.right, lvl + 1, maxLevel, True, result)


def deepestRightNodeRec(root):
    if root is None:
        return None
    result = [None]
    deepestRightNodeUtil(root, 0, [0], True, result)
    return result[0]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)
root.right.right.right = Node(8)
root.right.left.right.left = Node(9)
root.right.right.right.right = Node(10)

print(deepestRightNodeRec(root).data)
