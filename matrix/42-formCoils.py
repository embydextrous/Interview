# https://www.geeksforgeeks.org/form-coils-matrix/
from matrix import printS

def printCoils(N):
    coil1 = []
    coil2 = []
    step = 4 * N
    for i in range(step):
        coil1.append(step * i + 1)
        coil2.append(16 * N * N + 1 - coil1[-1])
    step -= 2
    toAdd = [1, -1 * 4 * N]
    flag = True
    while step != 0:
        for k in range(2):
            valueToAdd = toAdd[k]
            if not flag:
                valueToAdd *= -1
            for i in range(step):
                coil1.append(coil1[-1] + valueToAdd)
                coil2.append(16 * N * N + 1 - coil1[-1])
        step -= 2
        flag = not flag
    print(coil1[::-1])
    print(coil2[::-1])

N = 2
printCoils(N)


