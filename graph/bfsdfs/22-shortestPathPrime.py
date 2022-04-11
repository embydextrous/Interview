'''
Shortest path to reach one prime to other by changing single digit at a time.
Given two four digit prime numbers, suppose 1033 and 8179, we need to find the shortest path 
from 1033 to 8179 by altering only single digit at a time such that every number that we get 
after changing a digit is prime. For example a solution is 1033, 1733, 3733, 3739, 3779, 8779, 8179

Examples:

Input : 1033 8179
Output :6

Input : 1373 8017
Output : 7

Input  :  1033 1033
Output : 0
'''
from math import sqrt

def getPrimes(n):
    f = 10 ** (n - 1)
    t = 10 ** n
    primes = set([i for i in range(f, t)])
    for i in range(2, int(sqrt(t)) + 1):
        for j in range(f + i - f % i, t, i):
            if j in primes:
                primes.remove(j)
    primes.remove(f)
    return list(primes)

def hasOnlyOneDigitDifferent(a, b):
    c = 0
    if a % 10 == b % 10:
        c += 1
    a //= 10
    b //= 10
    if a % 10 == b % 10:
        c += 1
    a //= 10
    b //= 10
    if a % 10 == b % 10:
        c += 1
    a //= 10
    b //= 10
    if a % 10 == b % 10:
        c += 1
    return c == 3

def createGraph(primes):
    d = {}
    n = len(primes)
    for i in range(n):
        if primes[i] not in d:
            d[primes[i]] = []
        for j in range(i + 1, n):
            if hasOnlyOneDigitDifferent(primes[i], primes[j]):
                d[primes[i]].append(primes[j])
                if primes[j] not in d:
                    d[primes[j]] = [primes[i]]
                else:
                    d[primes[j]].append(primes[i])
    return d

def bfs(g, x, y):
    q1, q2 = [x], []
    visited = set()
    visited.add(x)
    c = 0
    result = {}
    found = False
    while len(q1) > 0:
        while len(q1) > 0:
            p = q1.pop(0)
            if p == y:
                found = True
                break
            for q in g[p]:
                if q not in visited:
                    result[q] = p
                    q2.append(q)
                    visited.add(q)
        q1, q2 = q2, q1
        if found:
            break
        c += 1
    s = []
    i = y
    while i != x:
        s.append(i)
        i = result[i]
    s.append(x)
    print(s[::-1])
    return c

def findPath(n, x, y):
    if x == y:
        return 0
    primes = getPrimes(n)
    g = createGraph(primes)
    return bfs(g, x, y)

N = 4
X = 1033
Y = 8179
print(findPath(N, X, Y))