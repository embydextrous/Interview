def countStrictlyIncreasingSubArrays(a):
    n = len(a)
    count = 0
    l = 0
    r = 1
    while r < n:
        if r < n - 1 and a[r] < a[r+1]:
            r += 1
        else:
            count += ((r-l+1) * (r-l)) // 2
            l = r = r + 1
    return count

a = [1, 2, 3, 3, 4, 5, 6, 6, 7]
print(countStrictlyIncreasingSubArrays(a))