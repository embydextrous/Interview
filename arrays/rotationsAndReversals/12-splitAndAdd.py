# Same as left rotate except we don't take mod now in case k > length of array
def reverse(a, l, r):
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

def splitAndAdd(a, k):
    n = len(a)
    if k >= n - 1:
        return
    reverse(a, 0, k-1)
    reverse(a, k, n-1)
    reverse(a, 0, n-1)

a = [1, 2, 3, 4, 5, 6, 7]
splitAndAdd(a, 2)
print(a)