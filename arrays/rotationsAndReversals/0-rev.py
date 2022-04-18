def maxHammingDistance(a):
    n = len(a)
    s = a + a
    mhd = 0
    mhdIndex = 0
    for i in range(1, n-1):
        chd = 0
        for j in range(n):
            if s[j] != s[i+j]:
                chd += 1
        if chd > mhd:
            mhd = chd
            mhdIndex = i
    return (mhd, s[mhdIndex:mhdIndex + n])

a = [1, 1, 2, 1, 2]
print(maxHammingDistance(a))