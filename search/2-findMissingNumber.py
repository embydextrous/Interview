# https://www.geeksforgeeks.org/find-the-missing-number/

# Similar Problems
# https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/
# 

def findMissingNumber(arr):
    n = len(arr)
    xor = 0
    for i in range(1, n + 2):
        xor ^= i
        if i - 1 < n:
            xor ^= arr[i-1]
    return xor

arr = [3, 1, 7, 6, 5, 2, 8]
print(findMissingNumber(arr))