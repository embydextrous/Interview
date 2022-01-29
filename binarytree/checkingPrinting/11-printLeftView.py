from tree import Node

def printLeftView(root):
    if root is None:
        return
    q1, q2 = [root], []
    while len(q1) > 0:
        isFirstNode = True
        while len(q1) > 0:
            node = q1.pop(0)
            if isFirstNode:
                print(node.data, end = " ")
                isFirstNode = False
            elif len(q1) == 0:
                print(node.data, end = " ")
            if node.left:
                q2.append(node.left)
            if node.right:
                q2.append(node.right)
        q1, q2 = q2, q1
    print()

'''
            10
          /    \
        2        3 
      /   \    /   \
    7      8  12    15
                   /
                 14  
 '''   

root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)
printLeftView(root)