from matrix import printS

def rotateMatrix(m, k):
    for a in m:
        rotate(a, k % len(a))

def rotate(a, k):
    r = len(a) - 1
    reverse(a, 0, r)
    reverse(a, 0, k - 1)
    reverse(a, k, r)

def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
rotateMatrix(M, 3)
printS(M)