# https://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/
def findMaxRotationSum(a):
    n = len(a)
    sum = 0
    for i in a:
        sum += i
    rotationSum = 0
    for i in range(n):
        rotationSum += i * a[i]
    maxRotationSum = rotationSum
    print(rotationSum)
    for i in range(n-1):
        rotationSum = rotationSum - sum + n * a[i]
        print(rotationSum)
        maxRotationSum = max(maxRotationSum, rotationSum)
    return maxRotationSum

a = [8, 3, 1, 2]
findMaxRotationSum(a)