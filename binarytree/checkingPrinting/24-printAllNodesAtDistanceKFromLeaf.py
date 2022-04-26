from tree import Node

def printNodesAtDistanceKFromLeaf(root, path, k, visited):
    if root is None:
        return 0
    path.append(root)
    if root.left is None and root.right is None:
        if len(path) >= k + 1 and path[-k-1] not in visited:
            print(path[-k-1].data, end = " ")
            visited.add(path[-k-1])
    printNodesAtDistanceKFromLeaf(root.left, path, k, visited)
    printNodesAtDistanceKFromLeaf(root.right, path, k, visited)
    path.pop()


root = Node(8)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(16)
root.right = Node(10)
root.right.left = Node(21)
root.right.right = Node(14)
#root.left.left.left = Node(5)
#root.right.right.right = Node(11)

'''
        8
      /   \
     3     10
   /   \   / \
  1    16 21  14
 /              \      
5                11
'''

printNodesAtDistanceKFromLeaf(root, [], 2, set())
print()