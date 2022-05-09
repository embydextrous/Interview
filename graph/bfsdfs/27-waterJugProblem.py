'''
You are given an m liter jug and a n liter jug. Both the jugs are initially empty. The jugs don't have 
markings to allow measuring smaller quantities. You have to use the jugs to measure d liters of water 
where d is less than n. 

(X, Y) corresponds to a state where X refers to the amount of water in Jug1 and Y refers to the amount 
of water in Jug2.

Determine the path from the initial state (xi, yi) to the final state (xf, yf), where (xi, yi) is (0, 0) 
which indicates both Jugs are initially empty and (xf, yf) indicates a state which could be (0, d) or (d, 0).
'''
def findPath(m, n, sx, sy, fx, fy):
    q = [(sx, sy)]
    visited = {}
    visited[(sx, sy)] = (-1, -1)
    while len(q) > 0:
        (x, y) = q.pop(0)
        if x == fx and y == fy:
            break
        if (0, y) not in visited:
            visited[(0, y)] = (x, y)
            q.append((0, y))
        if (x, 0) not in visited:
            visited[(x, 0)] = (x, y)
            q.append((x, 0))
        if (n, y) not in visited:
            visited[(n, y)] = (x, y)
            q.append((n, y))
        if (x, m) not in visited:
            visited[(x, m)] = (x, y)
            q.append((x, m))
        toTransfer = min(x, m - y)
        if (x - toTransfer, y + toTransfer) not in visited:
            visited[(x - toTransfer, y + toTransfer)] = (x, y)
            q.append((x - toTransfer, y + toTransfer))
        toTransfer = min(y, n - x)
        if (x + toTransfer, y - toTransfer) not in visited:
            visited[(x + toTransfer, y - toTransfer)] = (x, y)
            q.append((x + toTransfer, y - toTransfer))
    if (fx, fy) not in visited:
        return "Not Possible"
    s = []
    (x, y) = (fx, fy)
    while (x, y) != (-1, -1):
        s.append((x, y))
        (x, y) = visited[(x, y)]
    return s[::-1]

n = 4
m = 3
sx = sy = 0
fx = 3
fy = 3
print(findPath(m, n, sx, sy, fx, fy))