import sys

def maxProfitInfiniteTrades(prices):
    n = len(prices)
    maxProfit = 0
    for i in range(1, n):
        if prices[i] > prices[i-1]:
            maxProfit += prices[i] - prices[i-1]
    return maxProfit 

# Selling fees applies on sell transaction
def maxProfitInfiniteTradesWithFee(prices, fee):
    cashout, cashin = prices[0], 0
    for i in range(1, len(prices)):
        temp = cashout
        cashout = min(cashout, prices[i] - cashin)
        cashin = max(cashin, prices[i] - temp - fee)
    return cashin

# Cannot buy for 1 day cool off period after selling
def maxProfitInfiniteTradesWithCoolOff(prices):
    cashout, cashin, cashincooloff = prices[0], 0, 0
    # lbs will update using lbs and lcds
    # lss will update using lbs and lss
    # lcds will update using lcds and lss
    for i in range(1, len(prices)):
        lastcashout, lastcashin = cashout, cashin
        cashout = min(cashout, prices[i] - cashincooloff)
        cashin = max(cashin, prices[i] - lastcashout)
        cashincooloff = max(cashincooloff, lastcashin)
    return cashin


def maxProfitSingleTrade(prices):
    minPrice = prices[0]
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
    return maxProfit

def maxProfitAtMostTwoTrades(prices):
    n = len(prices)
    profit = [0] * n
    maxPrice = prices[n-1]
    for i in range(n - 2, -1, -1):
        if prices[i] > maxPrice:
            maxPrice = prices[i]
        profit[i] = max(profit[i+1], maxPrice - prices[i])
    minPrice = prices[0]
    for i in range(1, n):
        if prices[i] < minPrice:
            minPrice = prices[i]
        profit[i] = max(profit[i-1], profit[i] + prices[i] - minPrice)
    return profit[n-1]

# Time Complexity - O(k*n^2)
def maxProfitMaxKTrades(prices, k):
    n = len(prices)
    dp = [[0 for j in range(n)] for i in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1]
            for m in range(j-1, -1, -1):
                if prices[j] - prices[m] + dp[i-1][m] > dp[i][j]:
                    dp[i][j] = prices[j] - prices[m] + dp[i-1][m]
    print(dp)
    return dp[k][n-1]

prices = [100, 180, 260, 310, 40, 535, 695]
print(maxProfitInfiniteTrades(prices))
print(maxProfitSingleTrade(prices))
#prices = [2, 30, 15, 10, 8, 25, 80]
print(maxProfitAtMostTwoTrades(prices))

a = [10, 15, 17, 20, 16, 18, 22, 20, 22, 20, 23, 25]
print(maxProfitInfiniteTradesWithFee(a, 3))
print(maxProfitInfiniteTradesWithCoolOff(a))
print(maxProfitMaxKTrades(a, 4))



# 655 655 655 655 655 160 0
# 655 735 815 865 865 865 865