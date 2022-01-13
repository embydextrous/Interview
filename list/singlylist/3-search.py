from ll import LinkedList, Node

def search(node, key):
    while node:
        if node.data == key:
            print(str(key) + " found in list")
            return
        node = node.next
    print(str(key) + " not found in list")

a = LinkedList()
for i in range(5, 10):
    a.append(i)

a.print()
for i in range(13):
    search(a.head, i)