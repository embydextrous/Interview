# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

def maxSum(a):
    incl = excl = 0
    for i in a:
        newExcl = max(incl, excl)
        incl = excl + i
        excl = newExcl
    return max(incl, excl)

a = [5,  5, 10, 40, 50, 35]
print(maxSum(a))
