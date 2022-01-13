from dll import DoublyLinkedList, Node

class Result:
    def __init__(self):
        self.count = 0
        self.triplets = []

    def print(self):
        print("Number of triplets: " + str(self.count))
        print("Triplets: " + str(self.triplets))

def countAndPrintTriplets(node, x):
    result = Result()
    if node is None:
        return result
    current, lastNode = node, node
    while lastNode.next:
        lastNode = lastNode.next
    while current and current.next and current.next.next:
        l, r = current.next, lastNode
        while l.data < r.data:
            if current.data + l.data + r.data == x:
                result.count += 1
                result.triplets.append((current.data, l.data, r.data))
                l, r = l.next, r.prev
            elif current.data + l.data + r.data < x:
                l = l.next
            else:
                r = r.prev
        current = current.next
    return result

a = DoublyLinkedList()
a.append(1)
a.append(2)
a.append(4)
a.append(5)
a.append(6)
a.append(8)
a.append(9)
a.print()
countAndPrintTriplets(a.head, 15).print()

            


