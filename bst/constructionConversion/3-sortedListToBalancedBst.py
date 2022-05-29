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
    if head.next is None:
        return head
    (prevMid, mid) = findMiddle(head)
    nextToMid = mid.next
    mid.next = None
    prevMid.next = None
    mid.left = sortedListToBalancedBST(head)
    mid.right = sortedListToBalancedBST(nextToMid)
    return mid

head = Node(1)
head.next = Node(3)
head.next.next = Node(6)
head.next.next.next = Node(7)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next = Node(10)
head.next.next.next.next.next.next.next = Node(11)
head.next.next.next.next.next.next.next.next = Node(12)
head.next.next.next.next.next.next.next.next.next = Node(14)
head.next.next.next.next.next.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next.next.next.next.next.next = Node(16)
head.next.next.next.next.next.next.next.next.next.next.next.next = Node(17)


root = sortedListToBalancedBST(head)
preorder(root)
print()