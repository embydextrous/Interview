def deleteMiddle(s, n, curr):
    if len(s) > 0:
        q = s.pop()
        deleteMiddle(s, n, curr + 1)
        if curr != n//2:
            s.append(q)

s = [1, 2, 3, 4, 5, 6]
deleteMiddle(s, len(s), 0)
print(s)
