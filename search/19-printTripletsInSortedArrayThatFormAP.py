from search import binarySearchUtil

# array is sorted, elements are distinct
# O(n^2)
def printTripletsInAP(a):
    n = len(a)
    for i in range(1, n - 1):
        l = 0
        r = n - 1
        while l < i and r > i:
            if a[l] + a[r] == 2 * a[i]:
                print(a[l], a[i], a[r])
                l += 1
                r -= 1
            elif a[l] + a[r] < 2 * a[i]:
                l += 1
            else:
                r -= 1

a = [2, 6, 9, 12, 17, 22, 31, 32, 35, 42]
printTripletsInAP(a)
