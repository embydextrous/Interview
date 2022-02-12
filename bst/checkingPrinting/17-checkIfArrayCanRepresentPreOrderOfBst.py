import sys

def check(pre):
    n = len(pre)
    if n == 0:
        return True
    mini = -sys.maxsize-1
    s = []
    for i in range(n):
        x = pre[i]
        if x < mini:
            return False
        while len(s) > 0 and s[-1] < x:
            mini = s.pop()
        s.append(x)
    return True
            
pre = [40, 30, 35, 20, 80, 100]
print(check(pre))
