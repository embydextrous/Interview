from bst import Node

def findClosestUtil(root, k, closestNode):
    if root:
        if root.data == k:
            closestNode[0] = root
            return
        if closestNode[0] is None:
            closestNode[0] = root
        elif abs(root.data - k) < abs(closestNode[0].data - k):
            closestNode[0] = root
        findClosestUtil(root.left, k, closestNode)
        findClosestUtil(root.right, k, closestNode)

def findClosest(root, k):
    closestNode = [None]
    findClosestUtil(root, k, closestNode)
    return closestNode[0]

'''
                9
              /   \
             4     17
           /   \     \
          3     6     22
               / \    /
              5   7  20      
'''
root = Node(9) 
root.left = Node(4) 
root.right = Node(17)
root.left.left = Node(3) 
root.left.right = Node(6)
root.left.right.left = Node(5) 
root.left.right.right = Node(7) 
root.right.right = Node(22)
root.right.right.left = Node(20) 
k = 1
print(findClosest(root, k))