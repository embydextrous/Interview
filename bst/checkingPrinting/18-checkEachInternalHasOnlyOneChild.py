def check(pre):
    n = len(pre)
    if n == 0:
        return True
    mini = maxi = pre[-1]
    for i in range(n-2, -1, -1):
        if pre[i] < mini:
            mini = pre[i]
        elif pre[i] > maxi:
            maxi = pre[i]
        else:
            return False
    return True

pre = [20, 10, 11, 13, 12]
print(check(pre))