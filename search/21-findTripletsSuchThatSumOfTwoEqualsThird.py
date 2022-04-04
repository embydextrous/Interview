from search import binarySearchUtil

def findTriplets(a):
    n = len(a)
    c = 0
    for i in range(n - 2):
        if i != 0 and a[i] == a[i-1]:
            continue
        for j in range(i + 1, n - 1):
            if a[i] + a[j] > a[n-1]:
                continue
            idx = binarySearchUtil(a, j + 1, n - 1, a[i] + a[j])
            if idx != -1:
                print(a[i], a[j], a[idx])            

a = [1, 2, 4, 7, 9, 10, 12, 15, 18]
findTriplets(a)