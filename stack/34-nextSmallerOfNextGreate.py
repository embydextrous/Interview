def nextGreater(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return a[-1]
    s = [0]
    result = [-1] * n
    for i in range(1, n):
        x = a[i]
        if len(s) > 0 and x > a[s[-1]]:
            while len(s) > 0 and x > a[s[-1]]:
                result[s.pop()] = i
        s.append(i)
    return result

def nextSmaller(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return a[-1]
    s = [0]
    result = [-1] * n
    for i in range(1, n):
        x = a[i]
        if len(s) > 0 and x < a[s[-1]]:
            while len(s) > 0 and x < a[s[-1]]:
                result[s.pop()] = i
        s.append(i)
    return result

def nextSmallerOfNextGreater(a):
    nextSmallerIndex = nextSmaller(a)
    nextGreaterIndex = nextGreater(a)
    for i in range(len(a)):
        ngIndex = nextGreaterIndex[i]
        if ngIndex == -1:
            print(str(a[i]) + " -> " + str(-1))
        else:
            nsToNgIndex = nextSmallerIndex[ngIndex]
            if nsToNgIndex == -1:
                print(str(a[i]) + " -> " + str(-1))
            else:
                print(str(a[i]) + " -> " + str(a[nsToNgIndex]))

print(nextSmallerOfNextGreater([3, 1, 6, 2, 9, 4, 8, 5]))

