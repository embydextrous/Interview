# Problem boils down to max sum subArray of size k
# Also see, https://www.geeksforgeeks.org/find-subarray-least-average/
def maxAverageSubArrayOfSizeK(a, k):
    sum = 0
    maxSum = 0
    for i in range(k):
        sum += a[i]
    maxSum = sum
    for i in range(k, len(a)):
        enter, exit = a[i], a[i-k]
        sum += enter - exit
        maxSum = max(maxSum, sum)
    return maxSum / k

a = [1, 12, -5, -6, 50, 3]
print(maxAverageSubArrayOfSizeK(a, 4))