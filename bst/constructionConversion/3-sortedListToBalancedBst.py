from bst import Node, inorder, preorder

def findMiddle(root):
    fast, slow, prevSlow = root, root, None
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    return (prevSlow, slow)

def sortedListToBalancedBST(head):
    if head is None:
        return None
    (prevMid, mid) = findMiddle(head)
    nextToMid = mid.next
    mid.next = None
    if prevMid:
        prevMid.next = None
        mid.left = sortedListToBalancedBST(head)
    if nextToMid:
        mid.right = sortedListToBalancedBST(nextToMid)
    return mid

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

root = sortedListToBalancedBST(head)
preorder(root)
print()