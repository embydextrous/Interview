def interleave(q):
    n = len(q)
    q1, q2 = [], []
    for i in range(n//2):
        q1.append(q.pop(0))
    for i in range(n//2):
        q2.append(q.pop(0))
    for i in range(n//2):
        q.append(q1.pop(0))
        q.append(q2.pop(0))

q = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
interleave(q)
print(q)