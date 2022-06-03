from collections import defaultdict, deque

# 8, 9
# 11-20
# 21-30
# 21-34
# Climb Stairs
# Dominoes and Trominoes
# Stock Problems
from math import floor, sqrt

def unboundedKnapsack(W, weights, values):
    dp = [0] * (W + 1)
    for i in range(1, W + 1):
        for j in range(len(weights)):
            weight = weights[j]
            if weight <= i:
                dp[i] = max(dp[i], dp[i - weight] + values[j])
    print(dp)
    return dp[W]

values = [1, 4, 1, 6, 5, 4]
weights = [2, 3, 1, 6, 4, 5]
W = 10   
print(unboundedKnapsack(W, weights, values))
'''
0 1 2 4 5 6 8 9 10 12 13 
'''