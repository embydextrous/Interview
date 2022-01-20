# https://www.geeksforgeeks.org/minimum-sum-two-numbers-formed-digits-array-2/
import heapq

def minPossibleSum(digits):
    n1, n2 = 0, 0
    heapq.heapify(digits)
    while len(digits) > 0:
        n1 = n1 * 10 + heapq.heappop(digits)
        if len(digits) > 0:
            n2 = n2 * 10 + heapq.heappop(digits)
    return n1 + n2

digits = [5, 3, 0, 7, 4]
print(minPossibleSum(digits))