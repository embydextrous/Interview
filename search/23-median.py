# Median of two sorted arrays of same size

def median(a, b):
    n = len(a)
    return medianUtil(a, 0, n - 1, b, 0, n - 1)


def medianUtil(a, l1, r1, b, l2, r2):
    n = (r1 - l1) + 1
    if n == 1:
        return (a[l1] + b[l2]) / 2
    if n == 2:
        return (max(a[l1], b[l2]) + min(a[r1], b[r2])) / 2
    m1 = l1 + (r1 - l1) // 2
    m2 = l2 + (r2 - l2) // 2
    if a[m1] == b[m2]:
        if n % 2 == 1:
            return a[m1]
        else:
            return a[m1] + min(a[m1 + 1] + b[m2 + 1])
    elif a[m1] < b[m2]:
        if n % 2 == 0:
            return medianUtil(a, m1 + 1, r1, b, l2, m2)
        return medianUtil(a, m1, r1, b, l2, m2)
    else:
        if (n % 2 == 0):
            return medianUtil(a, l1, m1, b, m2 + 1, r2)
        return medianUtil(a, l1, m1, b, m2, r2)

arr1 = [1, 2, 7]
arr2 = [4, 6, 8]
print(median(arr1, arr2))