# Search where adjacent elements differ by at most 1
# Also, see https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/

def search(a, x, k):
    if k == 1:
        return search1(a, x)
    i = 0
    while i < len(a):
        if a[i] == x:
            return i
        i += (abs(x - a[i]) - 1) // k + 1
    return -1

def search1(a, x):
    i = 0
    while i < len(a):
        if a[i] == x:
            return i
        i += abs(x - a[i])
    return -1

a = [8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]
print(search1(a, 3))
a = [2, 4, 5, 7, 7, 6]
print(search(a, 6, 2))