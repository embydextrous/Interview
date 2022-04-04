from tree import Node

def levelOrder(root):
    if root is None:
        return
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        print(node.data, end = " ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print()


'''
'''
def levelOrder2(root):
    h = height(root)
    for i in range(h):
        printCurrentLevel(root, i)
        print()

def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 0:
        print(root.data, end=" ")
    else:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)


def height(root):
    if root is None:
        return 0
    else:
        lHeight, rHeight = height(root.left), height(root.right)
        return max(lHeight, rHeight) + 1

root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.right = Node(5)

levelOrder2(root)
print(height(root))