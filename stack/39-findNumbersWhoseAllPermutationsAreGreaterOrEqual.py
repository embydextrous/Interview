def findNumbers(n):
    if n <= 9:
        return n
    q = [i for i in range(1, 10)]
    c = 0
    continueScan = True
    while continueScan:
        k = q.pop(0)
        c += 1
        r = k % 10
        for i in range(r, 10):
            num = k * 10 + i
            if num > n:
                continueScan = False
                break
            q.append(num)
    return c + len(q)

print(findNumbers(20))
        

