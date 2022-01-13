def reverse(q, k):
    s = []
    while len(s) < k and len(q) > 0:
        s.append(q.pop(0))
    while len(s) > 0:
        q.append(s.pop())
    print(q)
    if k < len(q):
        for i in range(len(q) - k):
            q.append(q.pop(0))

a = [1, 2, 3, 4, 5, 6, 7]
reverse(a, 3)
print(a)
