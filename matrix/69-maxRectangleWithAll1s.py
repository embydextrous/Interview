from matrix import printS

def prevSmallerIndex(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return [-1]
    s = [n-1]
    result = [-1] * n
    for i in range(n-2, -1, -1):
        x = a[i]
        if len(s) > 0 and a[s[-1]] > x:
            while len(s) > 0 and a[s[-1]] > x:
                result[s.pop()] = i
        s.append(i)
    return result

def nextSmallerIndex(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return [-1]
    s = [0]
    result = [-1] * n
    for i in range(1, n):
        x = a[i]
        if len(s) > 0 and a[s[-1]] > x:
            while len(s) > 0 and a[s[-1]] > x:
                result[s.pop()] = i
        s.append(i)
    return result

def maxAreaHistogram(a):
    n = len(a)
    nsi = nextSmallerIndex(a)
    psi = prevSmallerIndex(a)
    areas = [0] * n
    for i in range(n):
        left = i if psi[i] == -1 else i - psi[i] - 1
        right = n - i - 1 if nsi[i] == -1 else nsi[i] - i - 1
        areas[i] = (1 + left + right) * a[i]
    return max(areas)

def maxRectangeWithAllOnes(M):
    R, C = len(M), len(M[0])
    # Form Histogram
    for i in range(1, R):
        for j in range(C):
            if M[i][j] == 1:
                M[i][j] = 1 + M[i-1][j]
    printS(M)
    maxRect = 0
    for row in M:
        maxRect = max(maxRect, maxAreaHistogram(row))
    return maxRect
            
M =     [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]

A = [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
     [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
     [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
     [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
     [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
     [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
     [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
     [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
     [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]

print(maxRectangeWithAllOnes(A))