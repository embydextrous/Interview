from tree import Node

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

def reverseAlternateLevels(root):
    if root is None or root.left is None:
        return
    q = [root.left, root.right]
    s = []
    while len(q) > 0:
        l, r = 0, len(q) - 1
        while l < r:
            q[l].data, q[r].data = q[r].data, q[l].data
            l += 1
            r -= 1
        while len(q) > 0:
            for i in range(2):
                node = q.pop(0)
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
        while len(s) > 0:
            for i in range(2):
                node = s.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
    print()



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

root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
reverseAlternateLevels(root)
levelOrder2(root)