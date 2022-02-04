from tree import Node

def lcaUtil(root, nodes, result):
    if root is None:
        return 0
    left = lcaUtil(root.left, nodes, result)
    right = lcaUtil(root.right, nodes, result)
    if left + right + (1 if root in nodes else 0) == len(nodes):
        result[0] = root
        return -1
    return left + right + (1 if root in nodes else 0)

def lca(root, nodes):
    if root is None:
        return None
    result = [None]
    lcaUtil(root, nodes, result)
    return result[0]

def deepestLeaves(root):
    if root is None:
        return None
    q1, q2 = [root], []
    leaves = set()
    while len(q1) > 0:
        leaves = set()
        while len(q1) > 0:
            node = q1.pop(0)
            if node.left is None and node.right is None:
                leaves.add(node)
            else:
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
        q1, q2 = q2, q1
    return leaves

def lcaOfDeepestLeaves(root):
    if root is None:
        return None
    leaves = deepestLeaves(root)
    return lca(root, leaves)

root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
#root.left.right.left = Node(4)
#root.left.right.right = Node(7)
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
print(lcaOfDeepestLeaves(root).data)