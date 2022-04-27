'''
Given Linked List Representation of Complete Binary Tree, construct the Binary tree. 
A complete binary tree can be represented in an array in the following approach.

10 -> 12 -> 15 -> 25 -> 30 -> 36

            10
          /    \
        12      15 
       /  \    /
      25  30  36   
'''
from tree import Node, inorder
from collections import deque

def construct(root):
    if root is None:
        return None
    q = deque([root])
    head = root
    while len(q) > 0:
        node = q.popleft()
        if head.next:
            node.left = head.next
            q.append(head.next)
            head = head.next
        if head.next:
            node.right = head.next
            q.append(head.next)
            head = head.next

root = Node(10)
root.next = Node(12)
root.next.next = Node(15)
root.next.next.next = Node(25)
root.next.next.next.next = Node(30)
root.next.next.next.next.next = Node(36)

construct(root)
inorder(root)
print()