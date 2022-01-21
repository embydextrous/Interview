# Array consists of rotation of strings
import sys

def minMoves(a):
    n = len(a[0])
    miniMoves = sys.maxsize
    for target in a:
        b = target + target
        count = 0
        for s in a:
            for i in range(n):
                if b[i:i+n] == s:
                    count += i
                    break
        miniMoves = min(count, miniMoves)
    return miniMoves

a = ["xzzwo", "zwoxz", "zzwox", "xzzwo"]
print(minMoves(a))