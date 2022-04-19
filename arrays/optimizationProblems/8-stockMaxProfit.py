def maxProfitInfiniteTrades(a):
    n = len(a)
    profit = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            profit += a[i] - a[i-1]
    return profit

# Effectively calculates max profit for each day
def maxProfitSingleTrade(a):
    minPrice = a[0]
    profit = 0
    for i in range(1, len(a)):
        if a[i] < minPrice:
            minPrice = a[i]
        else:
            profit = max(profit, a[i] - minPrice)
    return profit

# Cashout is minimized, cashin is maximized, fees applies on sell
def maxProfitInfiniteTradesWithFee(a, fee):
    cashout, cashin = a[0], 0
    for i in range(1, len(a)):
        tempCashout = cashout
        cashout = min(cashout, a[i] - cashin)
        cashin = max(cashin, a[i] - tempCashout - fee)
    return cashin

# Cool means cannot buy for 1 day after sell
def maxProfitInfiniteTradesCoolOff(a):
    cashout, cashin, cashinCoolOff = a[0], 0, 0
    for i in range(1, len(a)):
        lastCashin, lastCashout = cashin, cashout
        # Calculated from last cashout and cool off as you can't buy after sell
        cashout = min(lastCashout, a[i] - cashinCoolOff)
        # Calculated from last cashout and last cash in
        cashin = max(lastCashin, a[i] - lastCashout)
        # Calculated from last cashin and previous cashinCoolOff
        cashinCoolOff = max(lastCashin, cashinCoolOff)
    return cashin

def maxProfitTwoTrades(a):
    n = len(a)
    # profit[i] stores max profit for two trades till i
    profit = [0] * n
    # traverse left to right to find max profit in single trade till that point
    minPrice = a[0]
    for i in range(1, n):
        if a[i] < minPrice:
            minPrice = a[i]
            profit[i] = profit[i-1]
        else:
            profit[i] = max(profit[i-1], a[i] - minPrice)
    # traverse right to left to find max profit in single trade from that point to end
    # store it in same dp
    maxPrice = a[n-1]
    for i in range(n-2, -1, -1):
        if a[i] > maxPrice:
            maxPrice = a[i]
            profit[i] = max(profit[i+1], profit[i])
        else:
            profit[i] = max(profit[i+1], profit[i] + maxPrice - a[i])
    return profit[0]

# Space Complexity = O(k * n)
# Time Complexity = O(k * n ^ 2)
def maxProfitKTrades(a, k):
    n = len(a)
    profit = [[0 for i in range(n)] for j in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n):
            profit[i][j] = profit[i][j-1]
            for m in range(j):
                if profit[i-1][m] + a[j] - a[m] > profit[i][j]:
                    profit[i][j] = profit[i-1][m] + a[j] - a[m]
    return profit[k][n-1]

# Space Optimized Version - O(n)
def maxProfitKTrades2(a, k):
    n = len(a)
    profit = [[0 for i in range(n)] for j in range(2)]
    for i in range(1, k+1):
        for j in range(1, n):
            profit[1][j] = profit[1][j-1]
            for m in range(j):
                if profit[0][m] + a[j] - a[m] > profit[1][j]:
                    profit[1][j] = profit[0][m] + a[j] - a[m]
        profit[0], profit[1] = profit[1], profit[0]
    return profit[0][n-1]

# Time Optimized Version - O(nk)
def maxProfitKTrades3(a, k):
    n = len(a)
    profit = [[0 for i in range(n)] for j in range(2)]
    for i in range(1, k+1):
        prevDiff = -10 ** 9
        for j in range(1, n):
            prevDiff = max(prevDiff, profit[0][j - 1] - a[j - 1])
            profit[1][j] = max(profit[1][j-1], a[j] + prevDiff)
        profit[0], profit[1] = profit[1], profit[0]
    return profit[0][n-1]


a = [30, 40, 43, 50, 45, 20, 26, 40, 80, 50, 30, 15, 10, 20, 40, 45, 71, 50, 55]
print(maxProfitInfiniteTrades(a))
print(maxProfitSingleTrade(a))
print(maxProfitInfiniteTradesWithFee(a, fee = 3))
print(maxProfitInfiniteTradesCoolOff(a))
print(maxProfitTwoTrades(a))
print(maxProfitKTrades(a, 3))
print(maxProfitKTrades2(a, 3))
print(maxProfitKTrades3(a, 3))




