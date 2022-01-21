def leftRotateOne(a):
    n = len(a)
    x = a[0]
    for i in range(n - 1):
        a[i] = a[i+1]
    a[n-1] = x

def rightRotateOne(a):
    n = len(a)
    x = a[-1]
    for i in range(n-1, 0, -1):
        a[i] = a[i-1]
    a[0] = x

a = [1, 2, 3, 4, 5, 6, 7]
rightRotateOne(a)
print(a)
rightRotateOne(a)
print(a)
rightRotateOne(a)
print(a)