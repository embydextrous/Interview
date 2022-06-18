'''
There are 'p' balls of type P, 'q' balls of type Q and 'r' balls of type R. Using the balls we want to create a straight line such that no two balls of same type are adjacent.
Examples : 

Input  : p = 1, q = 1, r = 0
Output : 2
There are only two arrangements PQ and QP

Input  : p = 1, q = 1, r = 1
Output : 6
There are only six arrangements PQR, QPR,
QRP, RQP, PRQ and RPQ

Input  : p = 2, q = 1, r = 1
Output : 6
There are only six arrangements PQRP, QPRP,
PRQP, RPQP, PRPQ and PQPR
'''
def countUtil(p, q, r, last, memo):
    if p < 0 or q < 0 or r < 0:
        return 0
    if p == 1 and q == 0 and r == 0 and last == 0:
        return 0
    if p == 0 and q == 1 and r == 0 and last == 1:
        return 0
    if p == 0 and q == 0 and r == 1 and last == 2:
        return 0
    if p == 0 and q == 0 and r == 0:
        return 1
    if (p, q, r, last) in memo:
        return memo[(p, q, r, last)]
    if last == 0:
        memo[(p, q, r, last)] = countUtil(p, q - 1, r, 1, memo) + countUtil(p, q, r - 1, 2, memo)
    elif last == 1:
        memo[(p, q, r, last)] = countUtil(p - 1, q, r, 0, memo) + countUtil(p, q, r - 1, 2, memo)
    else:
        memo[(p, q, r, last)] = countUtil(p, q - 1, r, 1, memo) + countUtil(p - 1, q, r, 0, memo)
    return memo[(p, q, r, last)]

def count(p, q, r):
    memo = {}
    return countUtil(p-1, q, r, 0, memo) + countUtil(p, q - 1, r, 1, memo) + countUtil(p, q, r-1, 2, memo)
 
p = 2
q = 2
r = 2
print(count(p, q, r))
