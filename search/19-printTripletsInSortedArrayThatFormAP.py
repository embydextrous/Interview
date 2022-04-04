from search import binarySearchUtil

# array is sorted, elements are distinct
# O(nlogn) -> can be done in O(n) via hashing
def printTripletsInAP(a):
    n = len(a)
    c = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if a[j] + a[j] - a[i] > a[n - 1]:
                continue
            idx = binarySearchUtil(a, j + 1, n - 1, a[j] + a[j] - a[i])
            if idx != -1:
                print(a[i], a[j], a[idx])
            c += 1

a = [2, 6, 9, 12, 17, 22, 31, 32, 35, 42]
printTripletsInAP(a)
