from collections import deque

def sort(q):
    c = 0
    n = len(q)
    q1 = deque()
    while c != n:
        maxi = None
        while len(q) > c:
            x = q.popleft()
            if maxi == None:
                maxi = x
            elif x >= maxi:
                q1.append(maxi)
                maxi = x
            else:
                q1.append(x)
        q1.append(maxi)
        while len(q) > 0:
            q1.append(q.popleft())
        c += 1
        q1, q = q, q1
    return q

q = deque([9, 9, 1, 1])
print(sort(q))

q = [9, 1, 1, 6, 1, 3, 5, 6, 9, 4]
sort(q)
print(q)
            