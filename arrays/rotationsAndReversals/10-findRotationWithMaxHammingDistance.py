'''
Given an array of n elements, create a new array which is a rotation of given array and hamming distance
between both the arrays is maximum. 
Hamming distance between two arrays or strings of equal length is the number of positions at which the 
corresponding character(elements) are different.
Note: There can be more than one output for the given input. 
Examples: 

Input :  1 4 1
Output :  2
Explanation:  
Maximum hamming distance = 2.
We get this hamming distance with 4 1 1 
or 1 1 4 

Input :  N = 4
         2 4 8 0
Output :  4
Explanation: 
Maximum hamming distance = 4
We get this hamming distance with 4 8 0 2.
All the places can be occupied by another digit.
Other possible solutions are 8 0 2 4 and 0 2 4 8.  
'''

def findRotationWithMaxHammingDistance(a):
    n = len(a)
    maxHamDistance = 0
    maxHamIndex = 0
    b = a + a
    for i in range(1, n):
        c = 0
        for j in range(i, i + n):
            if b[j] != a[j-i]:
                c += 1
        print(c, b[i:i+n])
        if c > maxHamDistance:
            maxHamDistance = c
            maxHamIndex = i
    return (maxHamDistance, b[maxHamIndex: maxHamIndex+n])

a = [1, 1, 2, 1, 2]
print(findRotationWithMaxHammingDistance(a))
