# https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
# Also see, https://www.geeksforgeeks.org/return-a-pair-with-maximum-product-in-array-of-integers/

def maxProduct(a):
    n = len(a)
    if n == 3:
        return maxProductLen3(a)
    if n == 4:
        return maxProductLen4(a)
    if n == 5:
        return maxProductLen5(a)
    p = q = r = a[0]
    x = y = z = a[0]
    for i in range(1, n):
        if a[i] >= p:
            p, q, r = a[i], p, q
        elif a[i] >= q:
            q, r = a[i], q
        elif a[i] > r:
            r = a[i]
        if a[i] <= x:
            x, y, z = a[i], x, y
        elif a[i] <= y:
            y, z = a[i], y
        elif a[i] < z:
            z = a[i]
    return maxProductLen6([x, y, z, r, q, p])


def maxProductLen3(a):
    return a[0] * a[1] * a[2]

def maxProductLen4(a):
    a.sort()
    # 0 Negative or Only 1 Negative
    if a[0] >= 0 or a[1] >= 0:
        return a[1] * a[2] * a[3]
    # 2 Negative, 3 Negative - pick two larger negative elements and larger of +ve
    if a[2] >= 0 or a[3] >= 0:
        return a[0] * a[1] * a[3]
    # 4 Negative
    return a[1] * a[2] * a[3]

def maxProductLen5(a):
    a.sort()
    # 0 Negative or Only 1 Negative
    if a[0] >= 0 or a[1] >= 0:
        return a[2] * a[3] * a[4]
    # 2 Negative
    if a[2] >= 0:
        return max(a[0] * a[1] * a[4], a[2] * a[3] * a[4])
    # 3 Negative, 4 Negative
    if a[3] >= 0 or a[4] >= 0:
        return a[0] * a[1] * a[4]
    # 5 Negative
    return a[2] * a[3] * a[4]

def maxProductLen6(a):
    a.sort()
    # 0 Negative or Only 1 Negative
    if a[0] >= 0 or a[1] >= 0:
        return a[3] * a[4] * a[5]
    # 2 Negative, 3 Negative
    if a[2] >= 0 or a[3] >= 0:
        return max(a[0] * a[1] * a[5], a[3] * a[4] * a[5])
    # 4 Negative, 5 Negative
    if a[4] >= 0 or a[5] >= 0:
        return a[0] * a[1] * a[5]
    # 6 Negative
    return a[3] * a[4] * a[5]

a = [1, -4, 3, -6, 7, 0]
print(maxProduct(a))