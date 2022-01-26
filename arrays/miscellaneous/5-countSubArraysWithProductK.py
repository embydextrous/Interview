# https://www.geeksforgeeks.org/number-subarrays-given-product/

def countSubArraysWithAllOnes(a):
    n = len(a)
    count = 0
    l, r = 0, 0
    while r < n:
        if a[r] == 1:
            while r < n and a[r] == 1:
                r += 1
            count += ((r - l) * (r - l + 1)) // 2
            l = r
        else:
            l += 1
            r += 1
    return count


def countSubArrays(a, k):
    n = len(a)
    if k == 1:
        return countSubArraysWithAllOnes(a)
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

a = [1, 1, 1, 1, 1]
print(countSubArrays(a, 1))            


