from bst import Node, insert, preorder

def findMiddle(head):
    fast, slow, prevSlow = head, head, None
    while fast and fast.right:
        fast = fast.right.right
        prevSlow, slow = slow, slow.right
    return (prevSlow, slow)

def listToBalancedBst(head):
    if head is None:
        return None
    if head.right is None:
        return head
    prevMid, mid = findMiddle(head)
    prevMid.right = None
    nextToMid = mid.right
    mid.right = None
    mid.left = listToBalancedBst(head)
    mid.right = listToBalancedBst(nextToMid)
    return mid

def merge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.right = a
            tail = tail.right
            a = a.right
        else:
            tail.right = b
            tail = tail.right
            b = b.right
    if a:
        tail.right = a
    if b:
        tail.right = b
    next = head.right
    head.next = None
    return next

def inorder(root, tail):
    if root:
        inorder(root.left, tail)
        tail[0].right = root
        root.left = None
        tail[0] = root
        inorder(root.right, tail)

def mergeTrees(a, b):
    if a is None:
        return b
    if b is None:
        return a
    dummy1 = Node('*')
    dummy2 = Node('*')
    head1 = [dummy1]
    tail1 = [dummy1]
    head2 = [dummy2]
    tail2 = [dummy2]
    inorder(a, tail1)
    inorder(b, tail2)
    next1 = head1[0].right
    next2 = head2[0].right
    mergedHead = merge(next1, next2)
    return listToBalancedBst(mergedHead)

'''
            8
          /   \
        3      15 
       / \    /  \
      1   7  10   17
               \
                14

            11
          /    \
         9      12
        /         \
       6           16
'''
root1 = Node(8)
insert(root1, 3)
insert(root1, 15)
insert(root1, 10)
insert(root1, 17)
insert(root1, 14)
insert(root1, 1)
insert(root1, 7)

root2 = Node(11)
insert(root2, 9)
insert(root2, 6)
insert(root2, 12)
insert(root2, 16)

preorder(mergeTrees(root1, root2))
print()
