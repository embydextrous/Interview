# https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/

# Difficulty Mode - Extremely Hard
# Another Question Like this: 
# https://www.geeksforgeeks.org/find-maximum-difference-between-nearest-left-and-right-smaller-elements/

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
    return result

def prevSmallerIndex(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return [-1]
    result = [-1] * n
    s = [n-1]
    for i in range(n - 1, -1, -1):
        x = a[i]
        if len(s) > 0 and a[s[-1]] > x:
            while len(s) > 0 and a[s[-1]] > x:
                result[s.pop()] = i
        s.append(i)
    return result

def solution(a):
    n = len(a)
    nextSmaller = nextSmallerIndex(a)
    prevSmaller = prevSmallerIndex(a)
    result = [0] * (n + 1)
    for i in range(n):
        left = prevSmaller[i]
        right = nextSmaller[i] if nextSmaller[i] != -1 else n
        lg = right - left - 1
        result[lg] = max(result[lg], a[i])
    for i in range(n-1, 0, -1):
        result[i] = max(result[i], result[i+1])
    return result[1:]

a = [10, 20, 30, 50, 10, 70, 30]
print(solution(a))