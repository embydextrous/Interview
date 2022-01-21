def countEvenAndOddRotations(n):
    odd, even = 0, 0
    while n > 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    return (odd, even)

def countRotationsDivisibleBy10(n):
    c = 0
    while n > 0:
        if n % 10 == 0:
            c += 1
        n //= 10
    return c 

print(countEvenAndOddRotations(5634685573))
print(countRotationsDivisibleBy10(2703272000))