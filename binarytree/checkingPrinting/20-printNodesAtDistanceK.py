from tree import Node

def printNodesAtDistanceKDown(root, k):
    if root:
        if k == 0:
            print(root.data, end = " ")
            return
        printNodesAtDistanceKDown(root.left, k - 1)
        printNodesAtDistanceKDown(root.right, k - 1)

def printNodesAtDistanceK(root, source, k):
    if root is None:
        return -1
    if root == source:
        printNodesAtDistanceKDown(root, k)
        return 0
    dl = printNodesAtDistanceK(root.left, source, k)
    if dl != -1:
        if dl + 1 == k:
            print(root.data, end = " ")
        else:
            printNodesAtDistanceKDown(root.right, k - dl - 2)
        return dl + 1
    dr = printNodesAtDistanceK(root.right, source, k)
    if dr != -1:
        if dr + 1 == k:
            print(root.data)
        else:
            printNodesAtDistanceKDown(root.left, k - dr - 2)
        return dr + 1
    return -1

def fillParentNode(root, lastNode, parentNode):
    if root:
        parentNode[root] = lastNode
        fillParentNode(root.left, root, parentNode)
        fillParentNode(root.right, root, parentNode)

def printNodesAtDistanceKIterative(root, source, k):
    if root is None:
        return
    parentNode = {}
    fillParentNode(root, None, parentNode)
    visited = set()
    q1, q2 = [source], []
    while len(q1) > 0 and k >= 0:
        while len(q1) > 0:
            node = q1.pop(0)
            visited.add(node)
            if k == 0:
                print(node.data, end = " ")
            if node.left and node.left not in visited:
                q2.append(node.left)
            if node.right and node.right not in visited:
                q2.append(node.right)
            if parentNode[node] and parentNode[node] not in visited:
                q2.append(parentNode[node])
        k -= 1
        q1, q2 = q2, q1


root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.left.right.left = Node(4)
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
printNodesAtDistanceKIterative(root, root.left.right, 3)
print()