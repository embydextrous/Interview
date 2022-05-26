def check(pre):
    n = len(pre)
    if n == 0:
        return True
    maxi = mini = pre[n-1]
    for i in range(n - 2, -1, -1):
        maxi = max(maxi, pre[i])
        mini = min(mini, pre[i])
        if pre[i] != maxi and pre[i] != mini:
            return False
    return True

pre = [20, 10, 11, 13, 12]
print(check(pre))