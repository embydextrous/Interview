from bst import Node, insert

def isSameBSTUtil(a, b, n, i1, i2, min, max):
    j, k = i1, i2
    while j < n:
        if a[j] > min and a[j] < max:
            break
        j += 1
    while k < n:
        if b[k] > min and b[k] < max:
            break
        k += 1
    if j == n and k == n:
        return True
    if (j == n) ^ (k == n) or a[j] != b[k]:
        return False
    return isSameBSTUtil(a, b, n, j + 1, k + 1, a[j], max) and isSameBSTUtil(a, b, n, j + 1, k + 1, min, a[j])
 
# A wrapper over isSameBSTUtil()
def isSameBST(a, b, n):
    return isSameBSTUtil(a, b, n, 0, 0, -10 ** 9, 10 ** 9)

a = [8, 3, 6, 1, 4, 7, 10, 14, 13]
b = [8, 10, 14, 3, 6, 4, 1, 7, 13]
n = len(a)
print(isSameBST(a, b, n))