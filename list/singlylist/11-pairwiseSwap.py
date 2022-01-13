from ll import LinkedList, Node

def pairwiseSwap(node):
    while node and node.next:
        node.data, node.next.data = node.next.data, node.data
        node = node.next.next
    
a = LinkedList()
for i in range(9):
    a.append(i)
a.print()
pairwiseSwap(a.head)
a.print()