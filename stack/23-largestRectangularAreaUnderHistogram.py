# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/


hist = [6, 2, 5, 4, 5, 1, 6]

def nextSmallerIndex(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return [-1]
    result = [-1] * n
    s = [0]
    for i in range(1, n):
        x = a[i]
        if len(s) > 0 and a[s[-1]] > x:
            while len(s) > 0 and a[s[-1]] > x:
                result[s.pop()] = i
        s.append(i)
    print(result)
    return result

def prevSmallerIndex(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return [-1]
    result = [-1] * n
    s = [n-1]
    for i in range(n - 2, -1, -1):
        x = a[i]
        if len(s) > 0 and a[s[-1]] > x:
            while len(s) > 0 and a[s[-1]] > x:
                result[s.pop()] = i
        s.append(i)
    print(result)
    return result

def findLargestArea(hist):
    n = len(hist)
    prevSmaller = prevSmallerIndex(hist)
    nextSmaller = nextSmallerIndex(hist)
    maxArea = 0
    for i in range(n):
        right = nextSmaller[i] - i - 1 if nextSmaller[i] != -1 else n - i - 1
        left = i - prevSmaller[i] - 1 if prevSmaller[i] != -1 else i
        area = hist[i] * (1 + left + right)
        maxArea = max(area, maxArea)
    return maxArea

print(findLargestArea(hist))

    