def checkIfBinaryRotation(x, y):
    x = x | x << 32
    while x > y:
        if x & y == y:
            return True
        x = x >> 1
    return False

a = "43290016"
print(checkIfKRotation("amazon", "zonama", 9))