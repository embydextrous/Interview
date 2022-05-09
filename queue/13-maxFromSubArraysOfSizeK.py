from collections import deque

def findMax(a, k):
    q = deque()
    n = len(a)
    for i in range(k):
        if i == 0:
            q.append(a[i])
        else:
            while len(q) > 0 and q[-1] < a[i]:
                q.pop()
            q.append(a[i])
    for i in range(k, n + 1):
        if len(q) > 0:
            print(q[0], end = " ")
        if i == n:
            break
        enter, exit = a[i], a[i-k]
        if exit == q[0]:
            q.popleft()
        while len(q) > 0 and q[-1] < enter:
            q.pop()
        q.append(enter)
    print()



a = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
findMax(a, 4)

