
# https://www.geeksforgeeks.org/binary-tree-set-1-introduction/
# https://www.geeksforgeeks.org/binary-tree-set-2-properties/
# https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/
# https://www.geeksforgeeks.org/enumeration-of-binary-trees/
# Full Binary Tree -> All nodes have either 0 or 2 children
# Complete Binary Tree -> All levels full except last and all nodes to extreme left (heap is a complete binary tree)
# Perfect Binary Tree -> All levels are completely filled
# Degenerate Tree -> Same performance as Linked List

# 9 Left Page 1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.data}"

def insert(root, data):
    if root is None:
        return Node(data)
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        else:
            node.left = Node(data)
            break
        if node.right:
            q.append(node.right)
        else:
            node.right = Node(data)
            break
    return root

def delete(root, key):
    if root is None:
        return
    if root.left is None and root.right is None:
        if root.key == key:
            return None
        else:
            return root
    keyNode = None
    q = [root]
    temp = None
    # finds lastmost right node
    # also finds note to delete
    while len(q) > 0:
        temp = q.pop(0)
        if temp.data == key:
            keyNode = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    # if there is a node to delete, copy temp data to it and delete temp node using deleteDeepest()
    if keyNode:
        x = temp.data
        deleteDeepest(root, temp)
        keyNode.data = x

def deleteDeepest(root, dNode):
    if root is None:
        return
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        if node is dNode:
            dNode = None
            return
        if node.right:
            if node.right is dNode:
                node.right = None
                return
            else:
                q.append(node.right)
        if node.left:
            if node.left is dNode:
                node.left = None
                return
            else:
                q.append(node.left)

        
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


# T(0) = 1, T(1) = 1, T(2) = 2, 
# T(3) = T(0) * T(2) + T(1) * T(1) + T(2) * T(0) = 2 + 1 + 2 = 5
# T(4) = T(0) * T(3) + T(1) * T(2) + T(2) * T(1) + T(3) * T(0) = 5 + 2 + 2 + 5 = 14