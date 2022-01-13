from ll import LinkedList, Node
from random import randint

def sort(l):
    head0 = tail0 = Node('*')
    head1 = tail1 = Node('*')
    head2 = tail2 = Node('*')
    while l.head:
        if l.head.data == 0:
            tail0.next = l.head
            l.head = l.head.next
            tail0, tail0.next = tail0.next, None
        elif l.head.data == 1:
            tail1.next = l.head
            l.head = l.head.next
            tail1, tail1.next = tail1.next, None
        else:
            tail2.next = l.head
            l.head = l.head.next
            tail2, tail2.next = tail2.next, None
    head0, head1, head2 = head0.next, head1.next, head2.next
    if head0:
        l.head = head0
        if head1:
            tail0.next = head1
            tail1.next = head2
    elif head1:
        l.head = head1
        tail1.next = head2
    else:
        l.head = head2

a = LinkedList()
for i in range(20):
    print()
a.print()
sort(a)
a.print()


