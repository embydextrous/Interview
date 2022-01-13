def stockSpan(prices):
    n = len(prices)
    span = [0] * n
    span[0] = 1
    s = [0]
    for i in range(1, n):
        while len(s) > 0 and prices[s[len(s) - 1]] <= prices[i]:
            s.pop()
        span[i] = i + 1 if len(s) == 0 else i - s[len(s) - 1]
        s.append(i)
    return span

a = [100, 80, 60, 70, 60, 75, 85]
print(stockSpan(a))

