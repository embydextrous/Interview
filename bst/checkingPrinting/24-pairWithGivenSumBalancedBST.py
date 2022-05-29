from tabnanny import check
from bst import Node, insert

def pairWithSum(root, sum):
    s1 = []
    s2 = []
    a, b = root, root
    while True:
        if a or b:
            if a:
                s1.append(a)
                a = a.left
            if b:
                s2.append(b)
                b = b.right
        else:
            if len(s1) == 0 or len(s2) == 0:
                break
            l = s1.pop()
            r = s2.pop()
            if l == r:
                return False
            if l.data + r.data == sum:
                print(l.data, r.data)
                return True
            elif l.data + r.data < sum:
                s2.append(r)
                a = l.right
            else:
                s1.append(l)
                b = r.left
    return False

root = Node(15)

# 8, 10, 12, 15, 16, 20, 25

print(pairWithSum(root, 30))


