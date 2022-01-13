def reverse(q):
    s = []
    while len(q) > 0:
        s.append(q.pop(0))
    while len(s) > 0:
        q.append(s.pop())

q = [1, 2, 3, 4, 5]
reverse(q)
print(q)