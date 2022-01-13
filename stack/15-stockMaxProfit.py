import sys

def maxProfitInfiniteTrades(prices):
    n = len(prices)
    assert(n > 2)
    maxProfit = 0
    for i in range(n):
        if prices[i] > prices[i-1]:
            maxProfit += prices[i] - prices[i-1]
    return maxProfit

def maxProfitSingleTrade(prices):
    minPrice = prices[0]
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
    return maxProfit

def maxProfitMaxKTrades(prices, k):
    n = len(prices)
    profit = [[0 for i in range(n)] for i in range(k+1)]
    for i in range(1, k+1):
        prevDiff = -sys.maxsize-1
        for j in range(1, n):
            prevDiff = max(prevDiff, profit[i-1][j-1] - prices[j-1])
            profit[i][j] = max(profit[i][j-1], prevDiff + prices[j])
    return profit[k][n-1]


prices = [100, 180, 260, 310, 40, 535, 695]
print(maxProfitInfiniteTrades(prices))
print(maxProfitSingleTrade(prices))
prices = [10, 22, 5, 75, 65, 80]
print(maxProfitMaxKTrades(prices, 2))