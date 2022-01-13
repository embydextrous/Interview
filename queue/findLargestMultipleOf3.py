def findLargestMultiple(a):
    a.sort()
    s = 0
    n = len(a)
    rem1_1, rem1_2, rem2_1, rem2_2 = None, None, None, None
    for i in range(n):
        x = a[i]
        s += x
        if x % 3 == 1:
            if rem1_1 is None:
                rem1_1 = i
            elif rem1_2 is None:
                rem1_2 = i
        elif x == 2:
            if rem2_1 is None:
                rem2_1 = i
            elif rem2_2 is None:
                rem2_2 = i
    if s % 3 == 0:
        result = 0
        for i in range(len(a) - 1, -1, -1):
            result = result * 10
            result += a[i]
        return result
    elif s % 3 == 1:
        if rem1_1 is not None:
            result = 0
            for i in range(len(a) - 1, -1, -1):
                if i != rem1_1:
                    result = result * 10
                    result += a[i]
            return result
        elif rem2_1 is not None and rem2_2 is not None:
            result = 0
            for i in range(len(a) - 1, -1, -1):
                if i != rem1_1 and i != rem2_2:
                    result = result * 10
                    result += a[i]
            return result
        else:
            return -1
    else:
        if rem2_1 is not None:
            result = 0
            for i in range(len(a) - 1, -1, -1):
                if i != rem2_1:
                    result = result * 10
                    result += a[i]
            return result
        elif rem1_1 is not None and rem1_2 is not None:
            result = 0
            for i in range(len(a) - 1, -1, -1):
                if i != rem1_1 and i != rem1_2:
                    result = result * 10
                    result += a[i]
            return result
        else:
            return -1

a = [2, 5, 5, 6, 9]
print(findLargestMultiple(a))

