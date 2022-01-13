from ll import LinkedList, Node

# https://www.geeksforgeeks.org/how-to-sort-a-linked-list-that-is-sorted-alternating-ascending-and-descending-orders/

def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

def merge(a, b):
    head = tail = Node('*')
    while a and b:
        if a.data <= b.data:
            tail.next = a
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            tail = tail.next
            b = b.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head.next


def sort(node):
    head = tail = Node('*')
    current = node
    while current and current.next:
        next = current.next
        current.next = next.next
        tail.next = next
        tail = tail.next
        current = current.next
    tail.next = None
    a, b = node, reverse(head.next)
    merge(a, b)

a = LinkedList()
a.append(10)
a.append(40)
a.append(53)
a.append(30)
a.append(67)
a.append(12)
a.append(89)
a.print()
sort(a.head)
a.print()