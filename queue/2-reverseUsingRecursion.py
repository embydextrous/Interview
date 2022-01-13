def reverseUtil(q):
    if len(q) > 0:
        data = q.pop(0)
        q = reverseUtil(q)
        q.append(data)
    return q

q = [1, 2, 3, 4, 5]
reverseUtil(q)
print(q)