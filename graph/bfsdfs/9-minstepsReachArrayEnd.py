'''
Given an array containing one digit numbers only, assuming we are standing at first index, we need to 
reach to end of array using minimum number of steps where in one step, we can jump to neighbor indices
 or can jump to a position with same value.
In other words, if we are at index i, then in one step you can reach to, arr[i-1] or arr[i+1] or arr[K]
 such that arr[K] = arr[i] (value of arr[K] is same as arr[i])
Examples: 
 
Input : arr[] = {5, 4, 2, 5, 0}
Output : 2
Explanation : Total 2 step required.
We start from 5(0), in first step jump to next 5 
and in second step we move to value 0 (End of arr[]).

Input  : arr[] = [0, 1, 2, 3, 4, 5, 6, 7, 5, 4,
                 3, 6, 0, 1, 2, 3, 4, 5, 7]
Output : 5
Explanation : Total 5 step required.
0(0) -> 0(12) -> 6(11) -> 6(6) -> 7(7) ->
(18)               
'''
from collections import deque

def minSteps(a):
    n = len(a)
    graph = [[] for i in range(n)]
    visitedIndex = set()
    visitedIndex.add(0)
    for i in range(n):
        graph[a[i]].append(i)
    q = deque([[0, 0]])
    while len(q) > 0:
        idx, steps = q.popleft()
        if idx == n - 1:
            return steps
        if idx > 0 and idx - 1 not in visitedIndex:
            q.append([idx - 1, steps + 1])
        if idx + 1 not in visitedIndex:
            q.append([idx + 1, steps + 1])
        for i in graph[a[idx]]:
            if i not in visitedIndex:
                q.append([i, steps + 1])

a = [0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
print(minSteps(a))
