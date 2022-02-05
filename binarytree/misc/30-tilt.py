from tree import Node

def tiltUtil(root, tilt):
    if root is None:
        return 0
    left = tiltUtil(root.left, tilt)
    right = tiltUtil(root.right, tilt)
    tilt[0] += abs(left - right)
    return left + right + root.data

def tilt(root):
    if root is None:
        return 0
    t = [0]
    tiltUtil(root, t)
    return t[0]

'''
    4
   / \
  2   9
 / \   \
3   5   7
'''
root = Node(4)
root.left = Node(2)
root.right = Node(9)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(7)

print(tilt(root))
