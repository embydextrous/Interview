# https://www.geeksforgeeks.org/count-minimum-number-subsets-subsequences-consecutive-numbers/

def countSubsets(a):
    a.sort()
    n = len(a)
    c = 1
    for i in range(1, n):
        if a[i] - a[i-1] != 1:
            c += 1
    return c

a = [100, 56, 5, 6, 102, 58, 101, 57, 7, 103, 59]
print(countSubsets(a))