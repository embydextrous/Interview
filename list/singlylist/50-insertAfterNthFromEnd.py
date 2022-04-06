from ll import LinkedList, Node

def insert(l, newNode, k):
    current = l.head
    while current and k > 1:
        current = current.next
        k -= 1
    if current is None:
        newNode.next = l.head
        l.head = newNode
        return
    a = l.head
    while current.next:
        a = a.next
        current = current.next
    newNode.next = a.next
    a.next = newNode


a = LinkedList()
for i in range(10):
    a.append(i)
a.print()

insert(a, Node(12), 11)
a.print()
