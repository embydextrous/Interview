'''
Given an array 'arr' containing the weight of 'N' distinct items, and two knapsacks that can withstand 'W1' and 'W2' weights, the task is to find the sum of the largest subset 
of the array 'arr', that can be fit in the two knapsacks. It's not allowed to break any items in two, i.e an item should be put in one of the bags as a whole.
Examples: 
 

    Input : arr[] = {8, 3, 2} 
    W1 = 10, W2 = 3 
    Output : 13 
    First and third objects go in the first knapsack. The second object goes in the second knapsack. Thus, the total weight becomes 13.
    Input : arr[] = {8, 5, 3} 
    W1 = 10, W2 = 3 
    Output : 11 
'''
def doubleKnapsackUtil(a, W1, W2, idx, dp):
    if idx >= len(a):
        return 0
    if dp[W1][W2][idx] != -1:
        return dp[W1][W2][idx]
    fw1 = 0
    if W1 >= a[idx]:
        fw1 = a[idx] + doubleKnapsackUtil(a, W1 - a[idx], W2, idx + 1, dp)
    fw2 = 0
    if W2 >= a[idx]:
        fw2 = a[idx] + doubleKnapsackUtil(a, W1, W2 - a[idx], idx + 1, dp)
    dp[W1][W2][idx] = max(doubleKnapsackUtil(a, W1, W2, idx + 1, dp), fw1, fw2)
    return dp[W1][W2][idx]

a = [2, 4, 2]
W1 = 4
W2 = 4
n = len(a)
dp = [[[-1 for i in range(n)] for j in range(W2+1)] for j in range(W1+1)]
doubleKnapsackUtil(a, W1, W2, 0, dp)
print(dp[W1][W2][0])