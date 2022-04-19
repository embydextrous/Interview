def smallestSubArrayWithSumGreaterThan(a, x):
    n = len(a)
    minLen = (n + 1)
    i = 0
    j = 0
    sum = 0
    while i < n or j < n:
        if j < n and sum <= x:
            sum += a[j]
            j += 1
        if sum > k:
            print(i, j)
            minLen = min(j - i, minLen)
            sum -= a[i]
            i += 1
    return minLen

a = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
k = 300
print(smallestSubArrayWithSumGreaterThan(a, k))