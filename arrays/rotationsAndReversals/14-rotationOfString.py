
def leftRotation(s, k):
    n = len(s)
    k %= n
    s += s
    return s[k:k+n]

def rightRotation(s, k):
    n = len(s)
    k %= n
    s += s
    return s[n - k : 2 * n - k]

s = "1234567"
print(rightRotation(s, 0))