import sys

def largest(a):
    maxEle = -sys.maxsize-1
    for i in a:
        if i > maxEle:
            maxEle = i
    return maxEle

def twoLargest(a):
    maxi = secMaxi = -sys.maxsize-1
    for i in a:
        if i >= maxi:
            maxi, secMaxi = i, maxi
        elif i > secMaxi:
            secMaxi = i
    return (maxi, secMaxi)

def threeLargest(a):
    p = q = r = -sys.maxsize-1
    for i in a:
        if i >= p:
            p, q, r = i, p, q
        elif i >= q:
            q, r = i, q
        elif i > r:
            r = i
    return (p, q, r)

a = [6, 9, 0, 3, 2, 5, 1, 4]
print(largest(a))
print(twoLargest(a))
print(threeLargest(a))