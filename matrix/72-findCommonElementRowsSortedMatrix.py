from operator import index
from re import T


def findCommonElement(M):
    R, C = len(M), len(M[0])
    indexes = [0 for i in range(R)]
    while True:
        x = M[0][indexes[0]]
        maxEle = x
        areAllEqualToX = True
        for i in range(1, R):
            if M[i][indexes[i]] != x:
                areAllEqualToX = False
            if M[i][indexes[i]] > maxEle:
                maxEle = M[i][indexes[i]]
        if areAllEqualToX:
            return x
        for i in range(R):
            if M[i][indexes[i]] != maxEle:
                if indexes[i] == C - 1:
                    return -1
                indexes[i] += 1

M =    [[1, 2, 3, 4, 5 ],
        [1, 4, 5, 8, 10],
        [1, 5, 7, 9, 11],
        [1, 3, 5, 7, 9 ]]
    
print(findCommonElement(M))
