'''
Left Rotate
[1, 2, 3, 4, 5, 6, 7], k = 3
Left Rotate
[4, 5, 6, 7, 1, 2, 3]
Right Rotate
[5, 6, 7, 1, 2, 3, 4]
'''
def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

def leftRotate(a, k):
    n = len(a)
    k = k % n
    reverse(a, 0, k-1)
    reverse(a, k, n - 1)
    reverse(a, 0, n - 1)

def rightRotate(a, k):
    n = len(a)
    k = k % n
    reverse(a, 0, n - 1)
    reverse(a, 0, k - 1)
    reverse(a, k, n - 1)

a = [1, 2, 3, 4, 5, 6, 7]
rightRotate(a, 3)
print(a)