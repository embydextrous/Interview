import sys

def sort(q):
    n = len(q)
    s = 0
    lastMinEle = None
    minEle = sys.maxsize
    while s < n:
        minEle = sys.maxsize
        for i in range(n):
            x = q.pop(0)
            if lastMinEle is None:
                minEle = min(x, minEle)
            else:
                if x > lastMinEle:
                    minEle = min(x, minEle)
            q.append(x)
        c = 0
        for i in range(n):
            x = q.pop(0)
            if x == minEle:
                c += 1
            else:
                q.append(x)
        for i in range(c):
            q.append(minEle)
        s += c
        lastMinEle = minEle

q = [9, 1, 1, 6, 1, 3, 5, 6, 9, 4]
sort(q)
print(q)
            