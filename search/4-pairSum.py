# Check if a given array has a pair with sum x
# Also see, https://www.geeksforgeeks.org/check-exist-two-elements-array-whose-sum-equal-sum-rest-array/

# Hash based solution
# Time Complexity - O(n)
# Space Complexity - O(n)
def checkPairSum(arr, x):
    s = set()
    for i in arr:
        if x - i in s:
            return True
        s.add(i)
    return False

# Using sorting
# Time Complexity - O(nlogn)
# Space Complexity - O(1)
def hasPairSum(arr, x):
    arr.sort()
    l, r = 0, len(arr) - 1
    while l < r:
        if a[l] + a[r] == x:
            return True
        elif a[l] + a[r] > x:
            r -= 1
        else:
            l += 1
    return False

a = [3, 1, 8, 6, 9, 4, 11]
print(hasPairSum(a, 3))