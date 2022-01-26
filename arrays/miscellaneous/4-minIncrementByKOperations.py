# https://www.geeksforgeeks.org/minimum-increment-k-operations-make-elements-equal/
def minOperations(a, k):
    n = len(a)
    maxi = a[n-1]
    ops = 0
    for i in range(n-1):
        if abs(a[i] - a[i+1]) % k != 0:
            return -1
        maxi = max(maxi, a[i])
    for i in a:
        ops += (maxi - i) // k
    return ops

a = [4, 7, 19, 16]
print(minOperations(a, 3))
        