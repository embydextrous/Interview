def minRotations(s):
    n = len(s)
    a = s + s
    for i in range(1, n):
        if a[i:i+n] == s:
            return i
    return n

s = "abcdef"
print(minRotations(s))