# https://www.geeksforgeeks.org/smallest-multiple-of-a-given-number-made-of-digits-0-and-9-only/

def findFirstNumber(k):
    q = [9]
    while True:
        n = q.pop(0)
        if n % k == 0:
            return n
        q.append(n * 10)
        q.append(n * 10 + 9)

print(findFirstNumber(23))