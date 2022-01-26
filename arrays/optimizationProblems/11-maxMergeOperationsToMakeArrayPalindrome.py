# https://www.geeksforgeeks.org/find-minimum-number-of-merge-operations-to-make-an-array-palindrome/

def maxMergeOperations(a):
    l, r = 0, len(a) - 1
    count = 0
    while l < r:
        if a[l] == a[r]:
            l += 1
            r -= 1
        elif a[l] < a[r]:
            a[l+1] = a[l] + a[l+1]
            l += 1
            count += 1
        else:
            a[r-1] = a[r] + a[r-1]
            r -= 1
            count += 1
    return count

a = [11, 14, 15, 99]
print(maxMergeOperations(a))
