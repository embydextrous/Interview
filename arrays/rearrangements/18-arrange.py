'''
Given an array of numbers, arrange them in a way that yields the largest value. 
For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value. 
And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 
998764543431 gives the largest value.
'''
# 5 55 54 56
import math

def qsort(a, l, r):
    if l < r:
        p = partition(a, l, r)
        qsort(a, l, p - 1)
        qsort(a, p + 1, r)

def compare(x, y):
    p, q = int(math.log10(x)), int(math.log10(y))
    while True:
        a, b = x // (10 ** p), y // (10 ** q)
        print(a, b)
        if a != b:
            return a - b
        if p == 0 and q == 0:
            return a - b
        if p != 0:
            x -= a * (10 ** p)
        if q != 0:
            y -= b * (10 ** q)
        p = max(0, p - 1)
        q = max(0, q - 1)

def partition(a, l, r):
    i = l
    for j in range(l, r):
        if compare(a[j], a[r]) > 0:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

a = [1, 34, 3, 98, 9, 76, 45, 4]
qsort(a, 0, len(a) - 1)
print(a)


