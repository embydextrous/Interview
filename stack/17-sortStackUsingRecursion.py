def sort(s):
    if len(s) > 0:
        q = s.pop()
        sort(s)
        sortedInsert(s, q)

def sortedInsert(s, q):
    if len(s) == 0 or s[len(s) - 1] <= q:
        s.append(q)
    else:
        r = s.pop()
        sortedInsert(s, q)
        s.append(r)

a = [2, 6, 1, 3, 9, 5, 8]
sort(a)
print(a)

