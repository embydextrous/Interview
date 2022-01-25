def zeroesToBeFlipped(a, m):
    n = len(a)
    l = r = 0
    bestL = bestWindow = 0
    zeroCount = 0
    while r < n:
        if zeroCount <= m:
            if a[r] == 0:
                zeroCount += 1
            r += 1

        if zeroCount > m:
            if a[l] == 0:
                zeroCount -= 1
            l += 1

        if zeroCount <= m and r - l > bestWindow:
            bestL = l
            bestWindow = r - l
    zeroes = []
    for i in range(bestL, bestL + bestWindow):
        if a[i] == 0:
            zeroes.append(i)
    return zeroes

a = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
print(zeroesToBeFlipped(a, 2))
