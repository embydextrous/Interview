# https://www.geeksforgeeks.org/number-subarrays-given-product/

def countSubArraysWithAllOnes():
    return 0

def countSubArrays(a, k):
    n = len(a)
    if n == 1:
        return countSubArraysWithAllOnes()
    l = r = 0
    count = 0
    p = 1
    while r < n:
        if p < k:
            p *= a[r]
            r += 1
        if p > k:
            p //= a[l]
            l += 1
        if p == k:
            oneCount = 0
            i = 0
            while r + i < n:
                if a[r+i] != 1:
                    break
                oneCount += 1
                i += 1
            count = oneCount + 1
            p //= a[l]
            l += 1
            while p == k:
                count += oneCount + 1
                p //= a[l]
                l += 1
    return count

a = [1, 2, 3, 4, 1]
print(countSubArrays(a, 24))            


