# https://www.geeksforgeeks.org/minimum-cost-sort-matrix-numbers-0-n2-1/

def minCostForSorting(M):
    n = len(M)
    cost = 0
    for i in range(n):
        for j in range(n):
            key = M[i][j]
            x, y = key // n, key % n
            cost += abs(x-i) + abs(y-j)
    return cost

M = [[4, 7, 0, 3], # 6
     [8, 5, 6, 1], # 4
     [9, 11, 10, 2], # 6
     [15, 13, 14, 12]] # 6

print(minCostForSorting(M))