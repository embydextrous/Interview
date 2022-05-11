def deleteMiddle(s, n, i):
    if n == 0:
        return
    x = s.pop()
    if i == n // 2:
        return
    deleteMiddle(s, n, i + 1)
    s.append(x)

s = [1, 2, 3, 4, 5, 6]
deleteMiddle(s, len(s), 0)
print(s)
