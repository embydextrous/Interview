from collections import deque

def findMax(a, k):
    q = deque()
    for i in range(k):
        if len(q) == 0:
            q.appendleft(a[i])
        else:
            while len(q) > 0:
                if q[-1] > a[i]:
                    break
                q.pop()
            q.append(a[i])
    n = len(a)
    for i in range(k, n + 1):
        print(q[0], end = " ")
        if i == n:
            break
        enter, exit = a[i], a[i-k]
        if exit == q[0]:
            q.popleft()
        while len(q) > 0:
            if q[-1] > a[i]:
                break
            q.pop()
        q.append(enter)
    print()

a = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
findMax(a, 4)

