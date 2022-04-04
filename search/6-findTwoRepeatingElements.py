# https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/
# Also, see https://www.geeksforgeeks.org/find-repetitive-element-1-n-1/
# Also, see https://www.geeksforgeeks.org/find-the-two-numbers-with-odd-occurences-in-an-unsorted-array/
# Alse, see https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

def findTwoRepeatingElements(a, n):
    xor = 0
    for i in a:
        xor ^= i
    for i in range(1, n + 1):
        xor ^= i
    # we now have x^y in xor
    fsb = xor & (~(xor - 1))
    x = y = 0
    for i in a:
        if fsb & i == 0:
            x ^= i
        else:
            y ^= i
    # Yeah make sure to xor same number of elements which you did while finding xor.
    for i in range(1, n + 1):
        if fsb & i == 0:
            x ^= i
        else:
            y ^= i
    return (x, y)

a = [4, 2, 4, 5, 2, 3, 1]
print(findTwoRepeatingElements(a, 5))