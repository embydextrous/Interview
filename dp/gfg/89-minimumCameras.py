'''
Given a Binary Tree consisting of N nodes, the task is to find the minimum number of cameras required to monitor the entire tree such that every camera placed at any node can monitor the node itself, its parent, and its immediate children.

Examples:

Input:
             0
           /
        0
      /\
    0  0
Output: 1
Explanation:
             0
           /
        0  <———- Camera
      / \
   0   0
In the above tree, the nodes which are bold are the nodes having the camera. Placing the camera at the level 1 of the Tree can monitor all the nodes of the given Binary Tree.
Therefore, the minimum count of camera needed is 1.

Input:
             0
           /
        0
      /
    0 
      \
       0
Output: 2
'''
# Also see, https://www.geeksforgeeks.org/minimize-supply-of-corona-vaccines-for-n-houses-if-a-vaccine-is-sufficient-for-immediate-neighbours/

from tree import Node

def numCamerasUtil(root, count):
    if root is None:
        return 1
    left = numCamerasUtil(root.left, count)
    right = numCamerasUtil(root.right, count)
    if left == 1 and right == 1:
        return -1
    if left == -1 or right == -1:
        count[0] += 1
        return 0
    return 1    

def numCameras(root):
    if root is None:
        return 0
    count = [0]
    t = numCamerasUtil(root, count)
    if t == -1:
        count[0] += 1
    return count[0]

root = Node(0)

root.left = Node(1)
root.right = Node(2)

root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

root.left.right.left = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)

root.left.right.left.right = Node(9)
root.right.right.right.left = Node(10)

root.left.right.left.right.left = Node(11)
root.left.right.left.right.right = Node(12)


print(numCameras(root))

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(4)
root.right.right.right = Node(5)
root.right.right.right.right = Node(6)

print(numCameras(root))
    


