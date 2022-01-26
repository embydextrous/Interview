from unittest import result


# https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/

def mis(a):
    n = len(a)
    result = a[:]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and result[j] + a[i] > result[i]:
                result[i] = result[j] + a[i]
    return max(result)

a = [1, 101, 2, 3, 100, 4, 5]
print(mis(a))