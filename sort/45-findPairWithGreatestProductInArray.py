'''
Given an array of n elements, the task is to find the greatest number such that it is product of two 
elements of given array. If no such element exists, print -1. Elements are within the range of 1 to 10^5.
Examples : 

Input :  arr[] = {10, 3, 5, 30, 35}
Output:  30
Explanation: 30 is the product of 10 and 3.

Input :  arr[] = {2, 5, 7, 8}
Output:  -1
Explanation: Since, no such element exists.

Input :  arr[] = {10, 2, 4, 30, 35}
Output:  -1

Input :  arr[] = {10, 2, 2, 4, 30, 35}
Output:  4

Input  : arr[] = {17, 2, 1, 35, 30}
Output : 35
'''
def checkIfHasPairOfFactors(d, x):
    i = 1
    while i * i <= x:
        if x % i == 0:
            a, b = i, x // i
            if a == b:
                if d[a] == 2:
                    return True
            else:
                if a in d and b in d:
                    return True
        i += 1
    return False

def findPair(a):
    d = {x : a.count(x) for x in a}
    a.sort()
    for i in range(len(a) - 1, -1, -1):
        if checkIfHasPairOfFactors(d, a[i]):
            return a[i]
    return -1

a = [17, 2, 1, 35, 30]
print(findPair(a))