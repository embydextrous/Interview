def reverse(s):
    if len(s) > 0:
        v = s.pop()
        reverse(s)
        insert(s, v)

def insert(s, v):
    if len(s) > 0:
        q = s.pop()
        insert(s, v)
        s.append(q)
    else:
        s.append(v)

s = [1, 2, 3, 4, 5, 6, 7]
reverse(s)
print(s)