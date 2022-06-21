'''
Consider a 3 lane road of length N which includes (N + 1) points from 0 to N. A man starts at point 0 in the 2nd lane and wants to reach point N, 
but it is possible that there could be a barrier along the way. Given an array barrier[] of length (N + 1) where barrier[i](0 ≤ barrier[i] ≤ 3) defines
a barrier on the lane at point i. If barrier[i] is 0, then there is no barrier at that point. Otherwise, there is a barrier at the barrier[i]th lane at
the ith position. It is given that there will be at most one barrier in the 3 lanes at each point. The man can travel from ith point to (i + 1)th 
point only if there is no barrier at point (i + 1)th point. To avoid a barrier, that man just has to change to the lane where there is no barrier.

The task is to find the minimum number of changes in the lane made by the man to reach point N in any lane starting from point 0 and lane 2.

Examples:

Input: barrier[] = [0, 1, 0, 2, 3, 1, 2, 0]
Output: 3
Explanation:

Rules

1. You can only switch to adjacent lane in one go.
'''
INF = 10 ** 9

def minChangeLanes(barrier):
    a, b, c = 1, 0, 1
    n = len(barrier)
    for i in range(1, n):
        nextA = INF if barrier[i] == 1 else min(a, b + 1)
        nextB = INF if barrier[i] == 2 else min(a + 1, b, c + 1)
        nextC = INF if barrier[i] == 3 else min(b + 1, c)
        a, b, c = nextA, nextB, nextC
    return min(a, b, c)

a = [0, 1, 2, 3, 0]
print(minChangeLanes(a))