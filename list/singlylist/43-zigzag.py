from ll import LinkedList, Node

# https://www.geeksforgeeks.org/linked-list-in-zig-zag-fashion/

def zigzag(node):
    flag = True
    while node and node.next:
        if flag:
            if node.data > node.next.data:
                node.data, node.next.data = node.next.data, node.data
        else:
            if node.data < node.next.data:
                node.data, node.next.data = node.next.data, node.data
        flag = not flag
        node = node.next

a = LinkedList()
a.append(11)
a.append(15)
a.append(20)
a.append(5)
a.append(10)
a.print()
zigzag(a.head)
a.print()