'''
Super ugly numbers are positive numbers whose all prime factors are in the given prime list. 
Given a number n, the task is to find the nth Super Ugly number.
It may be assumed that a given set of primes is sorted. Also, the first Super Ugly number is 1 by convention.

Examples:  

Input  : primes[] = [2, 5]
         n = 5
Output : 8
Super Ugly numbers with given prime factors 
are 1, 2, 4, 5, 8, ...
Fifth Super Ugly number is 8

Input  : primes[] = [2, 3, 5]
         n = 50
Output : 243

Input : primes[] = [3, 5, 7, 11, 13]
        n = 9
Output: 21 
'''
def superugly(n, primes):
    primesIdx = [0] * len(primes)
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        mini = 10 ** 9
        for j in range(len(primes)):
            if dp[primesIdx[j]] * primes[j] < mini:
                mini = dp[primesIdx[j]] * primes[j]
        dp[i] = mini
        for j in range(len(primes)):
            if dp[primesIdx[j]] * primes[j] == mini:
                primesIdx[j] += 1
    return dp[n-1]

primes = [2, 5]
n = 5
print(superugly(n, primes))