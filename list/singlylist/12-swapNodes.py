from ll import LinkedList, Node

def swapNodes(l, a, b):
    if a == b:
        return
        
    prevX, x = None, l.head
    while x:
        if x.data == a:
            break
        prevX, x = x, x.next
    if not x:
        return
    
    prevY, y = None, l.head
    while y:
        if y.data == b:
            break
        prevY, y = y, y.next
    if not y:
        return

    if prevX != None:
        prevX.next = y
    else:
        l.head = y
 
    if prevY != None:
        prevY.next = x
    else:
        l.head = x
 
    x.next, y.next = y.next, x.next
    


a = LinkedList()
for i in range(10):
    a.append(i)
a.print()

swapNodes(a, 2, 3)
a.print()

