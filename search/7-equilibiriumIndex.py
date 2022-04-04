# An index whose leftSum == rightSum

# Also, see https://www.geeksforgeeks.org/maximum-equilibrium-sum-in-an-array/
# Can be also solved with prefix and suffix array but those will consume memory.

def findEqIndex(a):
    totalSum = 0
    for i in a:
        totalSum += i
    leftSum = 0
    for i in range(len(a)):
        if leftSum == totalSum - leftSum - a[i]:
            return i
        leftSum = leftSum + a[i]
    return -1

a = [-7, 1, 5, 2, -4, 3, 0]
print(findEqIndex(a))