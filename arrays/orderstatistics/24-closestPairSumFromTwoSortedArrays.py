# https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/
import sys

def closestSumPair(a1, a2, x):
    # Smallest sum is greater than equal to x
    if a1[0] + a2[0] >= x:
        return (a1[0], a2[0])
    # Largest sum is smaller than or equal to x
    if a1[len(a1) - 1] + a2[len(a2) - 1] <= x:
        return (a1[len(a1) - 1], a2[len(a2) - 1])
    l = 0
    r = len(a2) - 1
    minDiff = sys.maxsize
    pair = (l, r)
    while l < len(a1) and r > 0:
        diff = a1[l] + a2[r] - x
        if abs(diff) < minDiff:
            minDiff = abs(diff)
            pair = (a1[l], a2[r])
        if minDiff == 0:
            return pair
        if a1[l] + a2[r] < x:
            l += 1
        else:
            r -= 1
    return pair

ar1 = [1, 4, 5, 7]
ar2 = [10, 20, 30, 40]
x = 50
print(closestSumPair(ar1, ar2, x))

