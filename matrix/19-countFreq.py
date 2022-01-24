# Count frequency of k in a matrix of size n where matrix(i, j) = i+j
# Don't construct matrix

def count(n, k):
    if k < 2 or k > 2 * n:
        return 0
    if k <= n + 1:
        return k - 1
    return (2 * n - k) + 1

for i in range(1, 10):
    print(str(i) + ": ", end = " ")
    print(count(5, i))