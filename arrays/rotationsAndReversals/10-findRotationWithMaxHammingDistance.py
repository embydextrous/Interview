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
