# https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/

def maxSum(a, b):
    sum = 0
    sum1 = 0
    sum2 = 0
    L1, L2 = len(a), len(b)
    i, j = 0, 0
    while i < L1 and j < L2:
        if a[i] == b[j]:
            sum += max(sum1, sum2) + a[i]
            i += 1
            j += 1
            sum1 = sum2 = 0
        elif a[i] < b[j]:
            sum1 += a[i]
            i += 1
        else:
            sum2 += b[j]
            j += 1
    while i < L1:
        sum += a[i]
        i += 1
    while j < L2:
        sum += b[j]
        j += 1
    return sum

a = [2, 3, 7, 10, 12, 15, 30, 34]
b = [1, 5, 7, 8, 10, 15, 16, 19]
print(maxSum(a, b))

        