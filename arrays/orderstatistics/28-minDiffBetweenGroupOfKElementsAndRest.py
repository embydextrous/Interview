# https://www.geeksforgeeks.org/maximum-difference-group-k-elements-rest-array/
import heapq

def minDiff(a, k):
    arrSum = sum(a)
    kSmallestSum = sum(heapq.nsmallest(k, a))
    kLargestSum = sum(heapq.nlargest(k, a))
    return max(abs(arrSum - 2 * kSmallestSum), abs(arrSum - 2 * kLargestSum))

a = [1, -1, 3, -2, -3]
print(minDiff(a, 2))
