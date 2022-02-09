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

def construct(head):
    if head is None:
        return head
    q = [head]
    while head:
        root = q.pop(0)
        root.left = head.next
        head = head.next
        if head:
            q.append(head)
            root.right = head.next
        head = head.next
        if head:
            q.append(head)

root = Node(10)
root.next = Node(12)
root.next.next = Node(15)
root.next.next.next = Node(25)
root.next.next.next.next = Node(30)
root.next.next.next.next.next = Node(36)

construct(root)
inorder(root)
print()