def printRightRotation(a, k):
    n = len(a)
    for i in range(n):
        print(a[(i - k) % n], end = " ")
    print()

def printLeftRotation(a, k):
    n = len(a)
    for i in range(k, n + k):
        print(a[i % n], end = " ")
    print()

a = [1, 2, 3, 4, 5, 6, 7]
printLeftRotation(a, 3)