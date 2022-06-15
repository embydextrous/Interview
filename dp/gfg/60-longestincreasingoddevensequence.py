'''
Given an array of size n. The problem is to find the length of the subsequence in the given array such that all the elements of the subsequence are 
sorted in increasing order and also they are alternately odd and even. 
Note that the subsequence could start either with the odd number or with the even number.
Examples: 

Input : arr[] = {5, 6, 9, 4, 7, 8}
Output : 4
{5, 6, 7,8} is the required longest
increasing odd even subsequence which is the array itself in this case

Input : arr[] = {1, 12, 2, 22, 5, 30, 31, 14, 17, 11}
{1, 2, 5, 14, 17} is the required longest
increasing odd even subsequence
Output : 5
'''
def lioes(a):
    n = len(a)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and (a[i] & 1 != a[j] & 1) and dp[j] + 1 > dp[i]:
                dp[i] = 1 + dp[j]
    print(dp)
    return max(dp)

a = [1, 12, 2, 22, 5, 30, 31, 14, 17, 11]
print(lioes(a))