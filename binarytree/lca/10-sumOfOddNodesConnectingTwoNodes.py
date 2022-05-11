from tree import Node

def maxMinDown(root, a):
    if root is None:
        return (10 ** 9, -10 ** 9)
    if root == a:
        return (root.data, root.data)
    lMin, lMax = maxMinDown(root.left, a)
    if lMin != 10 ** 9:
        return (min(lMin, root.data), max(lMax, root.data))
    rMin, rMax = maxMinDown(root.left, a)
    if rMin != 10 ** 9:
        return (min(rMin, root.data), max(rMax, root.data))
    return (10 ** 9, -10 ** 9)

def maxMinUtil(root, a, b, result):
    if root is None:
        return (10 ** 9, -10 ** 9)
    if root == a:
        mini, maxi = maxMinDown(a, b)
        if mini != 10 ** 9:
            result[0] = (mini, maxi)
        return (root.data, root.data)
    if root == b:
        mini, maxi = maxMinDown(b, a)
        if mini != 10 ** 9:
            result[0] = (mini, maxi)
        return (root.data, root.data)
    lMin, lMax = maxMinUtil(root.left, a, b, result)
    rMin, rMax = maxMinUtil(root.right, a, b, result)
    print(root.data, lMax, lMin, rMax, rMin)
    if lMin != 10 ** 9 and rMin != 10 ** 9:
        result[0] = (min(lMin, rMin, root.data), max(lMax, rMax, root.data))
        return result[0]
    if lMin == 10 ** 9 and rMin == 10 ** 9:
        return (10 ** 9, -10 ** 9)
    return (min(lMin, root.data), max(lMax, root.data)) if lMin != 10 ** 9 else (min(rMin, root.data), max(rMax, root.data))

def maxMin(root, a, b):
    result = [10 ** 9, -10 ** 9]
    maxMinUtil(root, a, b, result)
    return result[0]

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(10)
root.left.right.right = Node(7)
root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(19)
root.right.right.right = Node(2)

'''
        8
      /   \
     3     10
   /   \     \
  1    16     14
      /  \   /  \
     4    7 19   2
'''
print(maxMin(root, root.left.right.left, root.right.right.left))

