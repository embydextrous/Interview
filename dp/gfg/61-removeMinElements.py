'''
Remove minimum elements from either side such that 2*min becomes more than max

Given an unsorted array, trim the array such that twice of minimum is greater than maximum in the trimmed array. Elements should be removed either end 
of the array.
Number of removals should be minimum.

Examples: 

arr[] = {4, 5, 100, 9, 10, 11, 12, 15, 200}
Output: 4
We need to remove 4 elements (4, 5, 100, 200)
so that 2*min becomes more than max.


arr[] = {4, 7, 5, 6}
Output: 0
We don't need to remove any element as 
4*2 > 7 (Note that min = 4, max = 8)

arr[] = {20, 7, 5, 6}
Output: 1
We need to remove 20 so that 2*min becomes
more than max

arr[] = {20, 4, 1, 3}
Output: 3
We need to remove any three elements from ends
like 20, 4, 1 or 4, 1, 3 or 20, 3, 1 or 20, 4, 1
'''
def removeMin(a):
    n = len(a)
    dp = [[[0, 0] if i != j else [a[i], a[i]] for i  in range(n)] for j in range(n)]
    maxi = 1
    for size in range(2, n + 1):
        for i in range(n-size+1):
            j = i + size - 1
            dp[i][j] = [min(dp[i+1][j][0], dp[i][j-1][0]), max(dp[i+1][j][1], dp[i][j-1][1])]
            if 2 * dp[i][j][0] > dp[i][j][1]:
                maxi = size
    return n - maxi

a = [4, 5, 100, 9, 10, 11, 12, 15, 200]
print(removeMin(a))
