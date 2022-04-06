'''
Given a linked list where every node represents a linked list and contains two pointers of its type: 
(i) Pointer to next node in the main list (we call it 'right' pointer in the code below) 
(ii) Pointer to a linked list where this node is headed (we call it the 'down' pointer in the code below). 
All linked lists are sorted. See the following example  

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45

Write a function flatten() to flatten the lists into a single linked list. 
The flattened linked list should also be sorted. For example, for the above input list, 
output list should be 5 -> 7 -> 8-> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 40 -> 45 -> 50. 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.v = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def print(self):
        print("head -> ", end="")
        current = self.head
        while current:
            print(str(current.data) + " -> ", end = "")
            current = current.next
        print("null")
'''
       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45
'''
def flattenList(node):
    while(node):
        if node.v:
            v = node.v
            node.v = None
            merge(node, v)
        node = node.next
        
def merge(a, b):
    tail = a
    a = a.next
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
            tail = tail.next
        else:
            tail.next = b
            b = b.v
            tail = tail.next
            tail.v = None
    if a:
        tail.next = a
    while b:
        tail.next = b
        b = b.v
        tail = tail.next
        tail.v = None


a = LinkedList()
a.append(5)
a.append(10)
a.append(19)
a.append(28)
a.head.v = Node(7)
a.head.v.v = Node(8)
a.head.v.v.v = Node(30)

a.head.next.v = Node(20)

a.head.next.next.v = Node(22)
a.head.next.next.v.v = Node(50)

a.head.next.next.next.v = Node(35)
a.head.next.next.next.v.v = Node(40)
a.head.next.next.next.v.v.v = Node(45)

flattenList(a.head)
a.print()