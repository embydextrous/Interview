from ll import LinkedList, Node
from random import randint

def sort(node):
    head0 = tail0 = Node('*')
    head1 = tail1 = Node('*')
    head2 = tail2 = Node('*')
    while node:
        if node.data == 0:
            tail0.next = node
            tail0 = tail0.next
            node = node.next
        elif node.data == 1:
            tail1.next = node
            tail1 = tail1.next
            node = node.next
        else:
            tail2.next = node
            tail2 = tail2.next
            node = node.next
    head0, head1, head2 = head0.next, head1.next, head2.next
    tail0.next, tail1.next, tail2.next = None, None, None
    if head0:
        if head1:
            tail0.next = head1
            tail1.next = head2
        else:
            tail0.next = head2
        return head0
    elif head1:
        tail1.next = head2
        return head1
    else:
        return head2

a = LinkedList()
a.append(2)
a.append(2)
a.append(0)
a.append(2)

a.print()
a.head = sort(a.head)
a.print()


