def checkBinaryRotation(a, b):
    x = a | a << 32 # Similar to concatenating string
    while x >= b:
        if x & 0xFFFFFFFF == b:
            return True
        x = x >> 1
    return False

b = 122
a = 2147483678

print(checkBinaryRotation(a, b))

