import heapq
from collections import deque

def maxFromSubArraysOfSizeK(a, k):
    h = [-1 * a[i] for i in range(k)]
    heapq.heapify(h)
    n = len(a)
    for i in range(k, n+1):
        print(-1 * h[0], end = " ")
        if i == n:
            break
        enter, exit = -1 * a[i], -1 * a[i - k]
        for j in range(k):
            if h[j] == exit:
                h[j] = enter
                heapq.heapify(h)
                break
    print()

def findMax(a, k):
    q = deque()
    for i in range(k):
        if len(q) == 0:
            q.appendleft(a[i])
        else:
            if a[i] < q[-1]:
                q.append(a[i])
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
maxFromSubArraysOfSizeK(a, 4)
findMax(a, 4)

