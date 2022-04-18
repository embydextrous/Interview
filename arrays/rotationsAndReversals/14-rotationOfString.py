
def leftRotation(s, k):
    n = len(s)
    k %= n
    s += s
    return s[k:k+n]

def rightRotation(s, k):
    n = len(s)
    k %= n
    k = n - k
    s += s
    return s[k:k+n]

s = "1234567"
print(rightRotation(s, 3))