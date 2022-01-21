import math

def generateAllRotations(n):
    k = int(math.log10(n))
    print(n, end = " ")
    for i in range(k):
        n = (n % 10) * (10 ** k) + n // 10
        print(n, end = " ")
    print()


n = 12345
generateAllRotations(n)

