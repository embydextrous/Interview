from collections import deque

hist = [6, 2, 5, 4, 5, 1, 6]

def nextSmallerIndex(a):
    n = len(a)
    result = [-1 for i in range(n)]
    s = [0]
    for i in range(1, n):
        while len(s) > 0 and a[s[-1]] > a[i]:
            result[s.pop()] = i
        s.append(i)
    return result

def prevSmallerIndex(a):
    n = len(a)
    result = [-1 for i in range(n)]
    s = [n-1]
    for i in range(n-2, -1, -1):
        while len(s) > 0 and a[s[-1]] > a[i]:
            result[s.pop()] = i
        s.append(i)
    return result

def largestArea(hist):
    n = len(hist)
    nsi = nextSmallerIndex(hist)
    psi = prevSmallerIndex(hist)
    maxArea = 0
    for i in range(n):
        left = i if psi[i] == -1 else i - psi[i] - 1
        right = n - i - 1 if nsi[i] == -1 else nsi[i] - i - 1
        maxArea = max(maxArea, (1 + left + right) * hist[i])
    return maxArea

hist = [6, 2, 5, 4, 5, 1, 6]
print(largestArea(hist))
